from requests import get
from sys import stdin
param = []

for line in stdin:
    param.append(line.strip())

url = param[0]
user_id = param[1]

try:
    req = get(url=f'http://{url}/users/{user_id}')
    user = req.json()
except Exception:
    print('Пользователь не найден')
else:
    email = user.get('email')
    last_name = user.get('last_name')
    first_name = user.get('first_name')
    username = user['username'] if user.get('username') else None
    for row in param[2:]:
        print(eval(f"f'{row}'"))