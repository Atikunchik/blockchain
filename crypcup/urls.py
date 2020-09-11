from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^convert/$', views.get_curruency, name='convert'),
]
