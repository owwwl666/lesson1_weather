import requests


def weather_forecast(cities, replacement):
    """"Выводим информацию о погоде в Лондоне, Шереметьево, Череповце"""
    for city in cities:
        url = f'https://ru.wttr.in/{city}'
        response = requests.get(url, params=replacement)
        response.raise_for_status()
        print(response.text)


def main():
    cities = ['Лондон',
              'Шереметьево',
              'Череповец'
              ]

    replacement = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': ''}

    weather_forecast(cities, replacement)


if __name__ == '__main__':
    main()
