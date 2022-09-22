from http.client import error
from lib2to3.pgen2.parse import ParseError
import requests
import json

url = "https://weatherapi-com.p.rapidapi.com/current.json"
context={}
querystring = {"q":"london"}

headers = {
	"X-RapidAPI-Key": "c1f94cdec6mshaefbef7657cd262p1906b5jsn84306654774f",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

try:        
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data=response.json()
    text=json.dumps(json_data)
        
    context={'text':text}
        
except response.status_code=='400':
    warning = "An Http Error occurred"
    context= {'warning':warning}

print(response.status_code)
print(response.text)