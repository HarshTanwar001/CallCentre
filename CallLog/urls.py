from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('initiate-call', views.call, name='call'),
    path('report', views.report, name='report'),
    path('call-report', views.generate, name='generate'),
]
