from django.urls import path
from . import views

urlpatterns = [
    path('add-country/', views.add_country, name='add_country'),
    path('add-state/', views.add_state, name='add_state'),
    path('add-city/', views.add_city, name='add_city'),
]
