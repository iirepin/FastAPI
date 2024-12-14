from fastapi import FastAPI # импортируем класс FastAPI
app = FastAPI() # создаем экземпляр класса FastAPI и инициализирует веб-приложение
@app.get('/hi') # декоратор который связхывает маршрут (URL) с функцие обработчиком
def greet(): # объявляем функцию, которая не принимает никаких аргументов
    return 'Hello? World?' # функция должна вернуть значение
if __name__ == "__main__": # определяет запущен ли скрипт напрямую или импортирован как модуль в другой скрипт
    import uvicorn # uvicorn - сервер для запуска веб приложений
    uvicorn.run("hello:app", reload=True) # запускает сервер с именем модуля - hello и app - объект приложения reload=True - автоматическая перезагрузка при изменении кода

    

