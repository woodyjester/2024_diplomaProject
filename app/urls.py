from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='home'),
    path('download/<str:type>/<str:id>/', views.download, name='download'),
    path('datasources/', views.datasources, name='datasources'),
    path('templates/', views.templates, name='templates'),
    path('rendering/', views.rendering, name='rendering'),
]
