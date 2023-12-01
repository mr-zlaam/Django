from django.shortcuts import render


# Create your views here.
def recipies(require):
    return render(require, "home.html")
