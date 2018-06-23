from django.contrib.auth.views import login, logout, logout_then_login
from django.urls import path, reverse
from . import views


app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),
]