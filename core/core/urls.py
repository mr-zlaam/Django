from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from vege.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", recipies),
    path("delete_recipe/<id>", delete_recipe, name="delete_recipe"),
    path("update_recipe/<id>", update_recipe, name="update_recipe"),
    path("login/", login_page, name="login_page"),
    path("register/", register_page, name="register_page"),
]
