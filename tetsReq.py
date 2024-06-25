# импортируем модуль
import requests

# отправляем запрос с заголовками по нужному адресу
req = requests.get("https://selectel.ru/blog/courses/")
# считываем текст HTML-документа
src = req.text
print(src)