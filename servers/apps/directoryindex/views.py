import os
import datetime
import glob
import mimetypes
import shutil
import zipfile
from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.template import loader
from directoryindex.models import UploadFile

class FileList():
    def __init__ (self):
        #MEDIA_ROOT = "/media/*"
        MEDIA_ROOT = "/home/support/python/note/django/servers/media/*"
        self.flist = glob.glob(MEDIA_ROOT)
    def getflist(self):
        return self.flist
        
def index(request):
    flist = FileList().getflist()
    mtime = range(len(flist))
    for i in range(len(flist)):
        mtime[i] = os.path.getmtime(flist[i])
        flist[i] = flist[i].replace("/home/support/python/note/django/servers/media/","/media/")
        
    template = loader.get_template('directoryindex/uploadfile_list.html')
    context = {'flist': flist}
    return HttpResponse(template.render(context, request))

def download(request, path):
    filepath = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filepath)
            return response
    raise Http404

def download_zip(request):
    file_pks = request.POST.getlist('zip')  # <input type="checkbox" name="zip"のnameに対応
    upload_files = UploadFile.objects.filter(pk__in=file_pks)

    response = HttpResponse(content_type='application/zip')
    file_zip = zipfile.ZipFile(response, 'w')
    for upload_file in upload_files:
        file_zip.writestr(upload_file.file.name, upload_file.file.read())

    # Content-Dispositionでダウンロードの強制
    response['Content-Disposition'] = 'attachment; filename="files.zip"'

    return response

