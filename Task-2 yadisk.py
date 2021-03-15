import requests

TOKEN = input()

response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={'path': 'kurskovp'},
                                headers={'Authorization': f'OAuth {TOKEN}'})

response_2 = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                        params={'path': 'kurskovp'},
                        headers={'Authorization': f'OAuth {TOKEN}'})

print(response_2.status_code)
print(response_2.json())

