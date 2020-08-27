from django.urls import path

from . import views


urlpatterns = [
    path('panel/subcategory/list/', views.subcategories_list, name='subcategories_list'),
    path('panel/subcategory/add/', views.add_subcategory, name='add_subcategory'),
]