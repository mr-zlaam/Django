from django.shortcuts import render, redirect

from .models import *


# Create your views here.
def recipies(request):
    if request.method == "POST":
        data = request.POST
        racipe_name = data.get("racipe_name")
        racipe_description = data.get("racipe_description")
        racipe_image = request.FILES.get("racipe_image")
        Recipe.objects.create(
            racipe_name=racipe_name,
            racipe_description=racipe_description,
            racipe_image=racipe_image,
        )
        return redirect("/")
    return render(request, "home.html")
