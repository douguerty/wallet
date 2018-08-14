from django.conf.urls import url, include
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('nova_conta/', views.RegistrationView.as_view(), name='nova_conta'),
]