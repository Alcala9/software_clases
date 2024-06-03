from django.urls import path
#from usuarios import views, views_categoria
from usuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('salir', LogoutView.as_view(), name='logout'),
    path('entrar', views.LoginView.as_view(), name='login'),
] 
