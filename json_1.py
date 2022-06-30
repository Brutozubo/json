logins = []
passwords = []
data_user = logins + passwords

import json

def register():

    logins.append(input("Создайте login: "))
    passwords.append(input("Создайте пароль: "))

    with open('data.json', 'w') as f:
        json.dump(data_user, f)

def login():

    login = input("Введите существующий login: ")
    password = input("Введите существующий пароль: ")

    with open('data.json', 'r') as f:
        data_user = json.load(f)

    if login in logins and password in passwords:
        print("Добро пожаловать!")
    else:
        print("Некорректные данные!")


while True:
    account_ans = input("Выберите пункт:  a)Зарегистрироваться     b)Войти в систему")
    if account_ans == "a":
        register()
    if account_ans == "b":
        login()
