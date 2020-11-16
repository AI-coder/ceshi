from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def upload_file(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile",None)
        if not myFile:
            return HttpResponse("no files for upload")
        destination = open(os.path.join(r'./upfile/upfile/',myFile.name),'wb')
        print(destination)
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload successful")
    else:
        return render(request,"upfile.html")