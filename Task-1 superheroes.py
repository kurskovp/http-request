import requests

response_1 = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
response_2 = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America')
response_3 = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')

data_1 = response_1.json()
data_2 = response_2.json()
data_3 = response_3.json()