import requests

response_1 = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
response_2 = requests.get('https://superheroapi.com/api/2619421814940190/search/Captain America')
response_3 = requests.get('https://superheroapi.com/api/2619421814940190/search/Thanos')

data_1 = response_1.json()
data_2 = response_2.json()
data_3 = response_3.json()

name_1 = data_1['results'][0]['name']
name_2 = data_2['results'][0]['name']
name_3 = data_3['results'][0]['name']


intell_1 = data_1['results'][0]['powerstats']['intelligence']
intell_2 = data_2['results'][0]['powerstats']['intelligence']
intell_3 = data_3['results'][0]['powerstats']['intelligence']

# print(name_1, intell_1)
# print(name_2, intell_2)
# print(name_3, intell_3)

a, b, c = (name_1, int(intell_1)), (name_2, int(intell_2)), (name_3, int(intell_3))
mx = a
if b >mx:
    mx = b
if c > mx:
    mx = c

print('Наивысший интелект имеет: ', mx)