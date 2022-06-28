
import json

login = []
passwd = []

def register():
    login.append(input("Выберите ваш login: "))
    passwd.append(input("Выберите ваш пароль: "))

def create_json():
    data_user = [{"login": login, "пароль": passwd}]
    with open('data.json', 'w') as f:
        json.dump(data_user, f)

def user_login():
    login = input("Введите ваш login: ")
    
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