import os
import datetime
import glob
import mimetypes
import shutil
import zipfile
from collections import defaultdict
from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.template import loader
from directoryindex.models import UploadFile

class FileList:
    def __init__ (self):
        print('init')

    def setpath(self, path):
        if path == "/":
            MEDIA_ROOT = "/home/support/python/note/django/servers/media/*"
        else:
            MEDIA_ROOT = "/home/support/python/note/django/servers/media/" + path + "*"
        self.fpath = glob.glob(MEDIA_ROOT)
        print(self.fpath)
        self.flist = list(range(len(self.fpath)))
        self.fsize = list(range(len(self.fpath)))
        self.mtime = list(range(len(self.fpath)))
        for i in range(len(self.fpath)):
            self.flist[i] = self.fpath[i].replace("/home/support/python/note/django/servers/media/","/media/")
            self.fsize[i] = os.path.getsize(self.fpath[i])
            self.mtime[i] = os.path.getmtime(self.fpath[i])
            self.mtime[i] = datetime.datetime.fromtimestamp(self.mtime[i]).strftime('%Y-%m-%d %H:%M:%S')
        self.fdict = defaultdict(list)
        for f,s,m in zip(self.flist, self.fsize, self.mtime):
            self.fdict[f].append(s)
            self.fdict[f].append(m)
        self.fdict = dict(self.fdict)
    def getfdict(self):
        return self.fdict
        
def index(request):
    path = request.path.replace('/directoryindex', '')
    aaa = FileList()
    aaa.setpath(path)
    fdict = aaa.getfdict()
    print(aaa.fdict)
        
    template = loader.get_template('directoryindex/uploadfile_list.html')
    context = {'fdict': fdict}
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

