from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "pengeluaran/index.html", context)


def tambahPengeluaran(request):
    context = {}
    return render(request, "pengeluaran/tambah_pengeluaran.html", context)
