from django.urls import path
from . import views
from .views import (HouseCreateView)


urlpatterns = [

    path('login/', views.loginView, name="login"),
    path('logout/', views.LogoutView, name="logout"), 
    path('register/', views.register_user, name="register"),
    path('', views.home, name='home'),
    path('predict_price', views.predict_price, name="predict_price"),
    path('houses', views.houses, name="houses"),
    path('news', views.newsBlogs, name='news'),
    path('house_create/', HouseCreateView.as_view(), name="house_create"),

]