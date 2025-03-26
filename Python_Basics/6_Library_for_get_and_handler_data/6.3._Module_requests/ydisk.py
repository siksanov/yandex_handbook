from requests_oauthlib import OAuth2Session
from requests import get, post, put, delete

client_id = "b976e8f04eec49c1b0ffdc0a5017d414"
client_secret = "c631586d67a6416c8f625992d5ebeae0"
auth_url = "https://oauth.yandex.ru/authorize"
token_url = "https://oauth.yandex.ru/token"
oauth = OAuth2Session(client_id=client_id)
authorization_url, state = oauth.authorization_url(auth_url, force_confirm="true")
print("Перейдите по ссылке, авторизуйтесь и скопируйте код:", authorization_url)
code = input("Вставьте одноразовый код: ")
token = oauth.fetch_token(token_url=token_url,
                          code=code,
                          client_secret=client_secret)
access_token = token["access_token"]
print(access_token)

headers = {"Authorization": f"OAuth {access_token}"}
r = get("https://cloud-api.yandex.net/v1/disk", headers=headers)
print(r.json())

params = {"path": "Тест API"}
r = put("https://cloud-api.yandex.net/v1/disk/resources", headers=headers, params=params)
print(r)

params = {"path": "Тест API/map.png"}
r = get("https://cloud-api.yandex.net/v1/disk/resources/upload",
        headers=headers, params=params)
print(r)
href = r.json()["href"]
files = {"file": open("map.png", "rb")}
r = put(href, files=files)
print(r)
