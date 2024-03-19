from django.urls import path

from lookup import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('about.html', views.about, name="about"),

]