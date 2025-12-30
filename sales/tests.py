from django.test import TestCase
from django.urls import reverse
from .models import Perfume


class PerfumeTests(TestCase):
    def setUp(self):
        Perfume.objects.create(name='Test Perfume', brand='Brand X', price=100000, stock=10)
        Perfume.objects.create(name='Sweet Rose', brand='RoseCo', price=150000, stock=5)
        Perfume.objects.create(name='Ocean Breeze', brand='Brand X', price=120000, stock=7)

    def test_list_view(self):
        resp = self.client.get(reverse('perfume-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Perfume')

    def test_show_all(self):
        resp = self.client.get(reverse('perfume-list') + '?all=1')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Sweet Rose')
        self.assertContains(resp, 'Ocean Breeze')

    def test_brand_filter(self):
        resp = self.client.get(reverse('perfume-list') + '?brand=RoseCo')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Sweet Rose')
        self.assertNotContains(resp, 'Ocean Breeze')

    def test_create(self):
        resp = self.client.post(reverse('perfume-create'), {
            'name': 'New Perfume',
            'brand': 'Brand Y',
            'price': '250000',
            'stock': '5'
        })
        self.assertEqual(resp.status_code, 302)  # redirect to detail
        self.assertTrue(Perfume.objects.filter(name='New Perfume').exists())

    def test_create_negative_price(self):
        resp = self.client.post(reverse('perfume-create'), {
            'name': 'Bad Perfume',
            'brand': 'Brand Bad',
            'price': '-1000',
            'stock': '1'
        })
        # form should be invalid -> return 200 with errors shown
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Harga harus bernilai positif')
        self.assertFalse(Perfume.objects.filter(name='Bad Perfume').exists())

    def test_create_with_image(self):
        from django.core.files.uploadedfile import SimpleUploadedFile
        gif = (
            b'GIF87a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
        )
        image = SimpleUploadedFile('test.gif', gif, content_type='image/gif')
        resp = self.client.post(reverse('perfume-create'), {
            'name': 'With Image',
            'brand': 'ImgCo',
            'price': '50000',
            'stock': '3',
            'image': image
        })
        self.assertEqual(resp.status_code, 302)
        p = Perfume.objects.get(name='With Image')
        self.assertTrue(p.image)
