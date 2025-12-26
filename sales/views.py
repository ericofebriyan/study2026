from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Perfume
from .forms import PerfumeForm


class PerfumeListView(ListView):
    model = Perfume
    template_name = 'sales/perfume_list.html'
    context_object_name = 'perfumes'
    paginate_by = 9
    ordering = ['-created_at']

    def get_queryset(self):
        qs = super().get_queryset()
        brand = self.request.GET.get('brand')
        if brand:
            qs = qs.filter(brand=brand)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['brands'] = Perfume.objects.order_by('brand').values_list('brand', flat=True).distinct()
        ctx['selected_brand'] = self.request.GET.get('brand', '')
        ctx['show_all'] = bool(self.request.GET.get('all'))
        return ctx

    def get_paginate_by(self, queryset):
        # If user requested to see all, disable pagination
        if self.request.GET.get('all'):
            return None
        return self.paginate_by


class PerfumeDetailView(DetailView):
    model = Perfume
    template_name = 'sales/perfume_detail.html'


class PerfumeCreateView(CreateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'sales/perfume_form.html'

    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, 'Parfum berhasil dibuat.')
        return resp


class PerfumeUpdateView(UpdateView):
    model = Perfume
    form_class = PerfumeForm
    template_name = 'sales/perfume_form.html'

    def form_valid(self, form):
        resp = super().form_valid(form)
        messages.success(self.request, 'Parfum berhasil diperbarui.')
        return resp


class PerfumeDeleteView(DeleteView):
    model = Perfume
    template_name = 'sales/perfume_confirm_delete.html'
    success_url = reverse_lazy('perfume-list')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, f'Parfum "{obj}" berhasil dihapus.')
        return super().delete(request, *args, **kwargs)

