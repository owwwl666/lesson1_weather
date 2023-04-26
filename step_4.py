import requests

cities = ['Лондон',
          'Шереметьево',
          'Череповец'
          ]

url_template = 'https://ru.wttr.in/{}?M?n?q?T'

for city in cities:
    url = url_template.format(city)
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
