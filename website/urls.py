from django.urls import path

from .views import index, details, create

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', details, name='details'),
    path('create/', create, name='create'),
]