from django.conf.urls import url 
from challenge import views 
 
urlpatterns = [ 
    url(r'^challenge/$', views.challenge_list),
    
]
