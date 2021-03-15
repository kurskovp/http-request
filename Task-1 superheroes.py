import requests

response_1 = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
response_2 = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America')
response_3 = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')

print(response_1.status_code)
print(response_2.status_code)
print(response_3.status_code)