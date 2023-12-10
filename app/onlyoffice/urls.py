from django.urls import path
from . import views

urlpatterns = [
    path('payload/', views.payload, name='payload'),
    path('callback/', views.callback, name='callback'),
    path('csrf-token/', views.get_csrf_token, name='csrf-token'),
    path('generate/', views.generate, name='generate'),
]