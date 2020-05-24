ip = input('Введите ip адрес: ')
oct1 = (ip.split('.'))[0]
oct1int = int(oct1)
if oct1int >0 and oct1int <224:
    print('Тип адреса: unicast')
elif oct1int > 223 and oct1int < 240:
    print ('Тип адреса: multicast')
elif ip == '255.255.255.255':
    print ('Тип адреса: local broadcast')
elif ip == '0.0.0.0':
    print ('Тип адреса: unassigned')
else:
    print ('Тип адреса: unused')
input()
