from vision.classifier import predict
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import os
def detect_dr(request):
    return render(request,'vision/diagnosis.html',{'result':False})

def detect_dr_result(request):
    image = request.FILES['fundus']
    fs = FileSystemStorage()
    try:
        vision = os.path.abspath(os.path.dirname(__file__))
        vision = os.path.join(vision,'uploads','fundus','uploaded.jpeg')
        os.remove(vision)
    except:
        pass
    filename = fs.save('vision/uploads/fundus/uploaded.jpeg', image)
    print(filename)
    prediction, percent_chance = predict()
    return render(request, 'vision/diagnosis.html', {'result': True,'prediction':prediction,'percent_chance':percent_chance})
