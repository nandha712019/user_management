from django.urls import path

from . import views

urlpatterns = [
    path('user_view/', views.UserView, name='user_view'),
    path('user_edit/', views.UserEdit, name='user_edit'),
    path('user_list/', views.UserList, name='user_list'),
    path('user_delete/<str:id>/', views.UserDelete, name='user_delete'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
