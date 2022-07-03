from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="expenses"),
    path("tambah_pengeluaran/", views.tambahPengeluaran, name="tambah_pengeluaran"),
]
