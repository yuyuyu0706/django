from django.urls import path
from . import views

app_name = 'lists'
 
urlpatterns = [
    path('', views.NWListView.as_view(), name='index'),
    # path('', views.IndexView.as_view(), name='index'),
]
