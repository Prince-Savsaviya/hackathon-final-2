import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'category=business&'
       'from=2022-10-15&'
       'to=2022-11-11'
       'apiKey=265085a4d0794fd4bac7064919b7010e')
response = requests.get(url)
print(response.json()['articles'])
