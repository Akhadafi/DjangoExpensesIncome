from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, "expense/index.html", context)


def add_expense(request):
    context = {}
    return render(request, "expense/add_expense.html", context)
