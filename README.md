# Описание
Данный проект представляет из себя скрипт, который позволяет сделать запрос на сайт прогноза погоды [wttr.in](https://wttr.in/) с помощью бибилотеки `requests` и получить информацию о погоде в трех городах: Лондон,Шереметьево и Череповец.

# Request
**requests** — это библиотека, с помощью которой можно делать запросы в интернет. Само слово “requests” переводится как запросы.
[Документация](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests)

# Установка библиотеки
Скрипт писался на Windows OS, поэтому для того,чтобы установить библиотеку необходимо выполнить команду

`python -m pip install requests` в командной строке.
# Обзор кода

```
import requests

cities = ['Лондон',
          'Шереметьево',
          'Череповец'
          ]

replacement = {'?': '%3F'}

url_template = 'https://ru.wttr.in/{}?M?n?q?T'

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, params=replacement)
    response.raise_for_status()
    print(response.text)
```

- Импортируем библиотеку
- Создаем список из городов, для которых хотим получить информацию о погоде
- Создаем url шаблон, в котором указываем ссылку на интересующий нас город из списка
- В цикле делаем запрос `requests.get(url, params=replacement)`. При этом словарь `replacement` отвечает за замену в url адресе запрещенных символов (ключ словаря) на escape-последовательность (значение словаря).
О кодировании url подробнее в [источнике](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters)
- Выводим результат в терминал

# Результаты
![Результат выполнения скрипта](https://dvmn.org/filer/canonical/1568003481/268/)





