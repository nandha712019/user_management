from django.urls import path

from . import views

urlpatterns = [
    path('user_view/', views.user_view, name='user'),
    path('admin_view/<int:id>/', views.admin_view, name='admin_view'),
]