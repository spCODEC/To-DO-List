from django.contrib import admin
from django.urls import path
from .views import home,delete_item,cross_off,uncross,edit_item
urlpatterns = [
    path('home',home,name = "home"),
    path('delete/<int:list_id>',delete_item,name = 'delete'),
    path('cross_off/<int:list_id>', cross_off, name='cross_off'),
    path('uncross/<int:list_id>', uncross, name='uncross'),
    path('edit/<int:list_id>',edit_item,name = 'edit'),
]
