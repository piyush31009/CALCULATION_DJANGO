from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def index(request):
    return render(request,'calculator.html')

def submitquery(request):
    querye=request.GET[ 'query']
    try:
        ans=eval(querye)
        mydict={
            'q':querye,
            'ans':ans,
            'error':False,
        }
        return render(request,"calculator.html",context=mydict)
    except:
        mydict={
            "error":True,
           
        }
    return render(request,"calculator.html",context=mydict)
