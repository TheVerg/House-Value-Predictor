from django.urls import path
from . import views
from .views import (HouseCreateView, NewsListView, NewsDetailView)


urlpatterns = [

    path('login/', views.loginView, name="login"),
    path('logout/', views.LogoutView, name="logout"), 
    path('register/', views.register_user, name="register"),
    path('', views.home, name='home'),
    path('predict_price', views.predict_price, name="predict_price"),
    path('houses', views.houses, name="houses"),
    path('house_create/', HouseCreateView.as_view(), name="house_create"),
    path('news/', NewsListView.as_view(), name="news"),
    path('news/<str:pk>/', NewsDetailView.as_view(), name="news-detail"),


]