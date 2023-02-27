from django.urls import path

from flower.views import download_catalog


app_name = 'flower'
urlpatterns = [
    path('download_catalog/', download_catalog, name='download_catalog'),
]
