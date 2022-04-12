from django.conf.urls import url
from django.urls  import path
from . import views 

app_name = 'learning_logs'

urlpatterns = [
    #Home page 
    path('', views.home, name='home'),
    path('topics', views.topics, name='topics'), 
] 