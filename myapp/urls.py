from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [
    # ex: /myapp/
    url(r'^$', views.enterOptions, name='enterOptions'),
    # ex: /myapp/results/
    url(r'^results/$', views.calcNgramCount, name='calcNgramCount'),
]