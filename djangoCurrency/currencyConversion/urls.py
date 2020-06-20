from django.urls import path
from . import views


urlpatterns = [
    path('', views.inputhome.as_view(), name = 'homepage'),
]
