from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('panel/setting/', views.site_setting, name='site_setting')
]