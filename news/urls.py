from django.urls import path, include

from . import views

app_name = 'news'
urlpatterns = [
    path('<str:title>/', views.news_details, name='details'),
    path('panel/news/', include([
        path('list/', views.news_list, name='list'),
        path('add/', views.add_news, name='add'),
        path('delete/<int:pk>/', views.delete_news, name='delete'),
        path('edit/<int:pk>/', views.edit_news, name='edit'),
    ]))
]
