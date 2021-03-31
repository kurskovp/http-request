import requests

TOKEN = input()

response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/download',
                       params={'path':'AgAAAABTHtuKAADLW-IkdUHVCU6JueXfIqBNDMo'},
                       headers = {'Authorization': f'OAuth {TOKEN}'})


print(response.status_code)
print(response.json())
href = response.json()['href']
with open('new_text') as f:
    requests.put(href, files = {'file': f})