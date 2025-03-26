from requests import get

# url = input()
# user_id = input()
message = ['Письмо для: {email}',
'Здравствуйте, {last_name} {first_name} ({username})',
'Мы рады сообщить вам о предстоящей акции!',
'Все подробности на нашем сайте',
'С уважением, команда тестового сервера!']

# while True:
#     try:
#         row = input()
#         message.append(row)
#     except Exception:
#         break

try:
    req = {
            "id": 1,
            "username": "first",
            "last_name": "Петрова",
            "first_name": "Елизавета",
            "email": "e.petrova@server.none"
          }
except Exception:
    print('Пользователь не найден')
else:
    email = req.get('email')
    last_name = req.get('last_name')
    first_name = req.get('first_name')
    username = req.get('username')
    for row in message:
        print(eval(f"f'{row}'"))