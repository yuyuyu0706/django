'''
from django.urls import path
from . import views #ここで先ほど作ったviews.pyを入れる

urlpatterns = [
    path('', views.index, name='index')
]
'''

from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='upload_list'),
    path('media/<str>', views.index, name='upload_list'),
    #path('media/[\w\-]+', views.index, name='upload_list'),
    # path('', views.UploadList.as_view(), name='upload_list'),
    # path('download/[\w\-]+)+', views.download, name='download'),
    #path('download/<int:pk>/', views.download, name='download'),
    path('download/zip/', views.download_zip, name='download_zip')
]
