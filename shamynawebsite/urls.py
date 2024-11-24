from django.urls import path, include
from shamynawebsite import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('left/', views.left, name='left'),  # Left page
    path('right/', views.right, name='right'),  # Right page
]

