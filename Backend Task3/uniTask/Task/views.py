from distutils.log import error
from multiprocessing import context
from urllib.error import HTTPError
from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

# Create your views here.
# This Task3 I have done Dynamically.
#  In task4 I have used form based data to call an API
def apiCall(request,pk):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    
   
    
    
    querystring={"q":pk}
    
    context={}
    headers = {
	"X-RapidAPI-Key": "c1f94cdec6mshaefbef7657cd262p1906b5jsn84306654774f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers,params=querystring)
        
    if response.status_code >= 400:
        warning = "**Enter A Valid Country Name**"
        context= {'warning':warning}
    else:        
        data=response.json()
        # data=json.dumps(json_data)
        context={'data':data,}
   
    
    # context={'text':text,'warning':warning}
    return render(request,'main.html',context)
    
