from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from vege.views import *

urlpatterns = [path("admin/", admin.site.urls), path("", recipies)]
