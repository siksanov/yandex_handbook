from requests import get, ConnectionError

params = {"ll": "37.677751,55.757718",
          "spn": "0.016457,0.00619",
          "l": "map"}
try:
    response = get("https://static-maps.yandex.ru/1.x/", params=params)
except ConnectionError:
    print("Проверьте подключение к сети.")
else:
    with open("map.png", "wb") as file:
        file.write(response.content)
