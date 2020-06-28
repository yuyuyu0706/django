'''
from django.urls import path
from . import views #ここで先ほど作ったviews.pyを入れる

urlpatterns = [
    path('', views.index, name='index')
]
'''

from django.urls import path,re_path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='upload_list'),
    #re_path('media/testdir', views.index, name='upload_list'),
    re_path('media(/[\w\-]+)+', views.index_next),
    #path('media/[\w\-]+', views.index, name='upload_list'),
    #path('download/[\w\-]+)+', views.download, name='download'),
    #path('download/<int:pk>/', views.download, name='download'),
    path('download/zip/', views.download_zip, name='download_zip')
]
