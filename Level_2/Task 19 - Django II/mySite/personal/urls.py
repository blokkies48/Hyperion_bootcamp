# Created urls and imported required files
from django.urls import path
from . import views

# Created url pattern
# the paths then in views it shows the html that should be returned
urlpatterns = [
    path('',views.index), 
    path('online_cv', views.online_cv),
    path('yum_yum',views.yum_yum),
]