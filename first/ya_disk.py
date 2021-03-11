import requests

TOKEN = 'AgAAAA16yaTAADLWBlKRwrYhUimmUWQ4zu39e4'

respons = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                       params={'path':'upload_file.txt'},
                       heanders = {'Authorizatijn': fr'OAuth {TOKEN}'})


print(respons.status_code)
print(respons.json())