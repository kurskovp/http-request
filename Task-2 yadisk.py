import requests

TOKEN = input()

response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                        params={'path': 'kurskovp'},
                        headers={'Authorization': f'OAuth {TOKEN}'})

response_2 = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                        params={'path': '0FoqeSA.gif&url=https%3A%2F%2Fcloud-api.yandex.net%2Fv1%2Fdisk%2Fresources%3Fpath%3Dkurskovp'},
                        headers={'Authorization': f'OAuth {TOKEN}'})
#
# response_3 = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                         params={'path': '0FoqeSA.gif&url=https%3A%2F%2Fcloud-api.yandex.net'
#                                         '%2Fv1%2Fdisk%2Fresources%3Fpath%3Dkurskovp'},
#                         headers={'Authorization': f'OAuth {TOKEN}'})


print(response_2.status_code)
print(response_2.json())
href = response_2.json()['href']
with open('0FoqeSA.gif', 'rb') as f:
    requests.put(href, files = {'file': f})

