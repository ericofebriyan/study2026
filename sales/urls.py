from django.urls import path
from . import views

urlpatterns = [
    path('', views.PerfumeListView.as_view(), name='perfume-list'),
    path('create/', views.PerfumeCreateView.as_view(), name='perfume-create'),
    path('<int:pk>/', views.PerfumeDetailView.as_view(), name='perfume-detail'),
    path('<int:pk>/update/', views.PerfumeUpdateView.as_view(), name='perfume-update'),
    path('<int:pk>/delete/', views.PerfumeDeleteView.as_view(), name='perfume-delete'),
]