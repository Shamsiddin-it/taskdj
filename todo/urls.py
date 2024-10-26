from django.urls import path
from .views import *


urlpatterns = [
    path('', show, name='all'),
    path('add/', add, name='add'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('get/<int:pk>', get, name='get'),
]
