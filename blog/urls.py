from django.urls import path
from . import views
urlpatterns = [
    path('posts/', views.BlogList.as_view(), name='blog-list'),
    path('posts/<int:pk>/', views.BlogDetail.as_view(), name='blog-detail'),
]