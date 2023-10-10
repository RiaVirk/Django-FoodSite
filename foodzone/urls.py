from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact_us, name="contact"),
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    path('menu/', views.all_dishes, name="all_dishes"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
]
