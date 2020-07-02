
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/', views.my_upload, name='upload'),
    url(r'^list/', views.my_list, name='list'),
]
