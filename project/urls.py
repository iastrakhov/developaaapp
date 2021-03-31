from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("photographs/", views.photographs, name = "photographs"),
    path('photographs/<int:photograph_id>/', views.info, name='info'),
]