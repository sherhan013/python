ip = input('Введите ip адрес: ')
if not '.' in ip:
    print('Неверный формат ip адреса')
elif len(ip.split('.')) < 4:
    print('Неверный формат ip адреса')
else:
    ip_octets = ip.split('.')
    ip_octets_int = []
    for oct in ip_octets:
        ip_octets_int.append(int(oct))
    A,B,C,D = ip_octets_int[0], ip_octets_int[1], ip_octets_int[2], ip_octets_int[3]
    if type(A) != int or A not in range(0,256) or type(B) != int or B not in range(0,256) or type(C) != int or C not in range(0,256) or type(D) != int or D not in range(0,256):
        print('Неверный формат адреса')
    else:
        oct1int = A
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
