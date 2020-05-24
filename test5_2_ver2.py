input_data = input('Введите ip-адрес сети в формате x.x.x.x/m: ')
network, mask = input_data.split('/')[0],input_data.split('/')[1]
octets = network.split('.')
A = octets[0]
B = octets[1]
C = octets[2]
D = octets[3]
Abin = f'{int(A):08b}'
Bbin = f'{int(B):08b}'
Cbin = f'{int(C):08b}'
Dbin = f'{int(D):08b}'
mask_bin = '1'*int(mask)+'0'*(32-int(mask))
maskA = mask_bin[0:8]
maskB = mask_bin[8:16]
maskC = mask_bin[16:24]
maskD = mask_bin[24:32]
maskA_dec=int(maskA,2)
maskB_dec=int(maskB,2)
maskC_dec=int(maskC,2)
maskD_dec=int(maskD,2)
line1 = f'{A:<8} {B:<8} {C:<8} {D:<8}'
line2 = f'{Abin:<8} {Bbin:<8} {Cbin:<8} {Dbin:<8}'
line3 = f'{maskA_dec:<8} {maskB_dec:<8} {maskC_dec:<8} {maskD_dec:<8}'
line4 = f'{maskA:<8} {maskB:<8} {maskC:<8} {maskD:<8}'
print('Network:')
print(line1)
print(line2)
print(' ')
print('Mask: ')
print(line3)
print(line4)

input()
