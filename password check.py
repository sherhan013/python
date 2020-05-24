login = input('Введите свой логин: ')
password = input ('Ввежите свой пароль: ')

while True:
    if len(password) < 7:
        print('Длина пароля менее 7 символов')

    elif login in password:
        print('Пароль содержит имя пользователя')

    elif '@' not in password:
        print('Пароль не содержит спецсимволов')

    else:
        print('Ваш пароль '+password+' подходит')
        break
    password = input ('Ввежите свой пароль: ')

input()
