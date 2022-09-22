# import requests

# url = "https://covid-19-statistics.p.rapidapi.com/reports"

# querystring = {"city_name":"New York"}

# headers = {
# 	"X-RapidAPI-Key": "c1f94cdec6mshaefbef7657cd262p1906b5jsn84306654774f",
# 	"X-RapidAPI-Host": "covid-19-statistics.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers,params=querystring)

# print(response.text)
import requests

url = "https://demo.stepzen.net/studio/spacex/__graphql"

payload="{\"query\":\"query MyQuery {\\n  spacex_missions(limit: 10) {\\n    id\\n    manufacturers\\n    name\\n  }\\n}\",\"variables\":{}}"
headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)



# json(javascript object Notation) is almost a python dictionary
#  JSON is the primary format in which data is passed back and forth to APIs, and most API servers will send their responses in JSON format.