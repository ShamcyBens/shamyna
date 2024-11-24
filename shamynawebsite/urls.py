from django.urls import path, include
from shamynawebsite import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('left/', views.left, name='left'),  # Left page
    path('right/', views.right, name='right'),  # Right page
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
