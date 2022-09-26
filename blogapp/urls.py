from django.urls import path
from blogapp import views

urlpatterns = [
    path ('', views.inicio, name="inicio"), 
    path ('blog/', views.blog,  name="blog"),
    path ('about/', views.about,  name="about"),
    path('crear_articulo/', views.articulo, name='crear_articulo'),

]