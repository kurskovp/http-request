import requests

response = requests.get('https://www.reddit.com/r/gifs.json', headers = {'User-Agent' : 'netology-client'})
print(response.status_code)
# print(response.headers)
# print(response.text)
# print(response.content)
data = response.json()
print(type(data))
posts = data['data']['children']

for post in posts:
    title = post['data']['title']
    url = post['data']['url']
    if 'imgur' not in url:
        continue
    with open(gif_name, mode='wb') as f:
        data_gif = requests.get(url)
        f.write(data_gif.content)
    print(title, url)

