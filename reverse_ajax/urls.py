from django.contrib import admin
from django.urls import path
from application import views

urlpatterns = [
    path('', views.home, name="home"),
    path('automate/', views.automate_run, name='automate_run'),
    path('admin/', admin.site.urls),
]
