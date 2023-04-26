import requests

url = 'https://ru.wttr.in/Череповец?M?n?q?T'
response = requests.get(url)
response.raise_for_status()
print(response.text)
