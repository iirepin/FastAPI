1.Запуск веб-приложения можно осуществлять двумя способами:
внешним - через терминал: uvicorn hello:app --reload, где hello - ссылка на файл, app - имя переменной
внутренним - через код в приложении смотри файл hello.py

Проверка в браузере:
http://localhost:8000/hi
Проверка с помощью requests смотри файл request.py
Проверка с помощью HTTPX смотри файл requests_httpx.py
Проверка с помощью HTTPie: http localhost:8000/hi
Проверка с помощью HTTPie c выводом только тела ответа: http -b localhost:8000/hi
Проверка с помощью HTTPie c выводом всех данных: http -v localhost:8000/hi
