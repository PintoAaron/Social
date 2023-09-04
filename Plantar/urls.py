from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('hello/', views.hello, name="hello"),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<int:id>', views.profile, name="profile"),
    path('login/', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout")
]
