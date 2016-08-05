from django.conf.urls import url

from shop import views

app_name = 'shop'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]