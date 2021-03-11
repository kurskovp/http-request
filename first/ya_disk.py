import requests


respons = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', params={'path':'upload_file.txt'})

print(respons.status_code)
print(respons.json())