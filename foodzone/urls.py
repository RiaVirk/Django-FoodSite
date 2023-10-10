from django.contrib import admin
from django.urls import path
from myapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    path('menu/', views.all_dishes, name="all_dishes"),
]
admin.site.site_header = "Food Zone | Admin"
admin.site.site_title = "Food Zone | Admin"
admin.site.index_title = "Food Zone | Admin"
