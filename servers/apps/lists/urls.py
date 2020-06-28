from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.MemberList.as_view(), name='member'),
]
