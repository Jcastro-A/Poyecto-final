from django.urls import path
from blogapp import views
from perfilapp.views import SignOutView
from perfilapp.views import SignInView, SignUpView, BienvenidaView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('', views.inicio, name="inicio"), 
    path ('blog/', views.blog,  name="blog"),
    path ('about/', views.about,  name="about"),
    path('crear_articulo/', views.articulo, name='crear_articulo'),
    path("iniciar_sesion/", SignInView.as_view(), name="sign_in"),
    path("bienvenida/", BienvenidaView.as_view(), name="bienvenida"),
    path("cerrar-sesion/", SignOutView.as_view(), name="sign_out"),
    path("registrate/", SignUpView.as_view(), name="sign_up"),
    path("crear_articulo/", views.articulo, name="crear_articulo"),    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)