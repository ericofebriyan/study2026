# Study2026 - Penjualan Parfum (CRUD)

A simple Django app to manage perfume sales (CRUD) implemented in the `sales` app.

## Fitur
- Daftar parfums
- Detail parfum
- Tambah / Ubah / Hapus parfum
- Validasi harga dan stok

## Cara menjalankan (development)

1. Buat virtualenv dan aktifkan (opsional jika sudah aktif)

   ```bash
   python -m venv env
   env\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. Install dependensi (project menggunakan Django 6.0)

   ```bash
   pip install -r requirements.txt  # jika tersedia; atau pip install django
   ```

3. Buat migrations dan terapkan

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. (Opsional) Buat superuser untuk mengakses admin

   ```bash
   python manage.py createsuperuser
   ```

5. Jalankan server

   ```bash
   python manage.py runserver
   ```

6. Akses aplikasi

   - Halaman utama: http://127.0.0.1:8000/
   - Daftar Parfum: http://127.0.0.1:8000/sales/
   - Admin: http://127.0.0.1:8000/admin/

## Testing

Jalankan unit tests:

```bash
python manage.py test sales
```

---

Electronics & code by contributor.