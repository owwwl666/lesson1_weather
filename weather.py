import requests

cities = ['Лондон',
          'Шереметьево',
          'Череповец'
          ]

replacement = {'?M': '', '?n': '', '?q': '', '?T': ''}

for city in cities:
    url = f'https://ru.wttr.in/{city}'
    response = requests.get(url, params=replacement)
    response.raise_for_status()
    print(response.text)
