from django.urls import path
from .           import views

urlpatterns = [
  path(''                , views.homePage     , name='homePage'),
  path('worker/<int:pk>/', views.worker_detail, name='worker_detail'),
]
