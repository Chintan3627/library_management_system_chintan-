from django.urls import path
from . import views
# from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration_page, name='registration'),
    path('login', views.login_page, name='login'),
    path('logout', views.LogoutView, name='logout'),
    # Add more URL patterns as needed
]