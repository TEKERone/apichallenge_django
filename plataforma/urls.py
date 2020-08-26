# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.conf.urls import url, include 
 
urlpatterns = [ 
    url(r'^', include('challenge.urls')), 
]