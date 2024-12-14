import requests # requests - отправляет запросы и обрабатывает ответы
r = requests.get("http://localhost:8000/hi/Mom") # отправляем запрос на сервер
r.json() # ответ преобразуем в формат json

