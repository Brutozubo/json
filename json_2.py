import json

def register(login, passwd):
    login = input('Введите login: ')
    passwd = input('Введите пароль: ')

    with open ('data.json') as f:
        initial = json.load(f)
    initial[login] = passwd

    with open('data.json', 'w') as f:
        json.dump(data_user, f)

def check_user(login):
    with open('data.json') as f:
        data_user = json.load(f)
    if login in data_user:
        print(f"Да, {login} существует")
        return True
    else:
        print(f"Нет такого {login}")
        return False
    
def login_function(login, passwd):
    with open ('data.json', 'r') as f:
        data_user = json.load(f)

    if login and passwd in data_user:
         print('Успешный вход!')
     else:
         print('Неверный логин или пароль')