from django.contrib import admin
from django.urls import path, include
from blogapp import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("blogapp/", include("blogapp.urls")),
    path("perfilapp/", include("perfilapp.urls")),

]


