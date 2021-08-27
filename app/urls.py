from django.urls import path

from . import views

urlpatterns = [
    path('user_view/', views.user_view, name='user_view'),
    path('user_edit/', views.user_edit, name='user_edit'),
    path('logout/', views.logout, name='logout'),
    path('admin_view/<int:id>/', views.admin_view, name='admin_view'),
]