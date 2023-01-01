from django.urls import path
from . import views

urlpatterns = [
    path('', views.smart_locks, name='smart_locks')
]
