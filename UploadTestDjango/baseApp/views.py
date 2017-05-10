from django.shortcuts import render,redirect
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from baseApp.models import upldData

def home(request):
    if request.method=="POST" and request.FILES['savefile']:
         fileP=request.FILES['savefile']
         fs=FileSystemStorage()
         fileX=fs.save(fileP.name, fileP)

         uploaded_url=fs.url(fileX)
         messages.success(request, 'File Uploaded Successfully!')
         return render(request, 'core/home.html', {'uploaded_url' : uploaded_url})

    return render(request, 'core/home.html')
