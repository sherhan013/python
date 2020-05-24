vlan_option = {'access':'Введите номер vlan: ', 'trunk':'Введите номера разрешенных vlan: '}
mode = input('Введите режим работы интерфейса (access/trunk): ')
interface = input('Введите тип и номер интерфейса: ')
vlan = input(vlan_option.get(mode))

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'

]
#Вводим переменнную switch - словарь с 2мя ключами access и trunk
switch = {'access': access_template, 'trunk': trunk_template}

#С помощью get обращаемся к словарю и получаем значение того элемента, который указали в get
#Так же с помощью JOIN из списка заданного в словаре получаем строку, разделенную \n и через format подставлем vlan

result = '\n'.join(switch[mode]).format(vlan)
print('Interface '+interface)
print(result)

input()
