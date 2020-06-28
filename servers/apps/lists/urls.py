from django.urls import path
from . import views

app_name = 'lists'
 
urlpatterns = [
    path('', views.NWListView.as_view(), name='member'),
]
