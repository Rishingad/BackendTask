from multiprocessing import context
from django.shortcuts import render
from .task1 import *
from django.http import HttpResponse


# Create your views here.
def task1(request,n1,n2):
    
    output=DecToBinary(n1,n2)
    context={'output':output,'n1':n1,'n2':n2}
    return render(request,'home.html',context)





