from django.urls import path
from . import views

urlpatterns = [
    path('add-country/', views.add_country, name='add_country'),
    path('add-state/', views.add_state, name='add_state'),
    path('add-city/', views.add_city, name='add_city'),
    
    #path('show-country/', views.show_country, name='show_country'),
    path('show-country/<str:country_name>/', views.show_country, name='show_country'),
    path('show-state/<str:country_name>/', views.show_state, name='show_state'),
    path('show-city/<str:country_name>/', views.show_city, name='show_city'),  # Updated for cities by country
    #path('show-city/<str:state_name>/', views.show_city, name='show_city'),
]
