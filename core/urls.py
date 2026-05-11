from django.urls import path

from . import views

app_name = 'urls'

urlpatterns = [
    path('', views.OriginalURLApiView.as_view(), name='original'),
    path('<pk>/', views.RedirectURLApiView.as_view(), name='redirect')
]
