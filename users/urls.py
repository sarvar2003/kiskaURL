from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='users-list'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('me/', views.MeView.as_view(), name='me')
]
