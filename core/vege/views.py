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
    queryset = Recipe.objects.all()
    context = {"recipies": queryset}
    return render(request, "home.html", context)


def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")


def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        racipe_name = data.get("racipe_name")
        racipe_description = data.get("racipe_description")
        racipe_image = request.FILES.get("racipe_image")

        queryset.racipe_name = racipe_name
        queryset.racipe_description = racipe_description
        if racipe_image:
            queryset.racipe_image = racipe_image

        queryset.save()
        return redirect("/")

    context = {"recipe": queryset}
    return render(request, "update_recipe.html", context)
