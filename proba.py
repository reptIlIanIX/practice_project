import logging
import json
from json import JSONDecodeError

logging.basicConfig(filename="basic.log")

try:
    path = "data.json"
    file = open(path)
    items = json.load(file)
    for item in items:
        print(item)
except FileNotFoundError:
    logging.exception("Ошибка доступа к файлу")

except JSONDecodeError:
    # Будет выполнено если файл найден, но не превращается из JSON
    logging.exception("Файл не удается преобразовать")