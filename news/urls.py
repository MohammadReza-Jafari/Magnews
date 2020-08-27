from django.urls import path

from . import views

urlpatterns = [
    path('<str:title>/', views.news_details, name='news_details'),
    path('panel/news/list/', views.news_list, name='news_list'),
    path('panel/news/add/', views.add_news, name='add_news'),
    path('panel/news/delete/<int:pk>/', views.delete_news, name='delete_news'),
    path('panel/news/edit/<int:pk>/', views.edit_news, name='edit_news')
]
