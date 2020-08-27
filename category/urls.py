from django.urls import path

from . import views


urlpatterns = [
    path('panel/category/list/', views.category_list, name='category_list'),
    path('panel/category/add/', views.add_category, name='add_category')
]