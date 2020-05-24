from sys import argv
network = argv[1]
mask = argv[2]
#input_data = input('Введите ip-адрес сети в формате x.x.x.x/m: ')
#network, mask = input_data.split('/')[0],input_data.split('/')[1]
octets = network.split('.')
A = octets[0]
B = octets[1]
C = octets[2]
D = octets[3]
Abin = f'{int(A):08b}'
Bbin = f'{int(B):08b}'
Cbin = f'{int(C):08b}'
Dbin = f'{int(D):08b}'
network_bin = f'{Abin}'+f'{Bbin}'+f'{Cbin}'+f'{Dbin}'
network_true = f'{network_bin[:int(mask)]}'+'0'*(32-int(mask))
Atrue = int(network_true[0:8],2)
Btrue = int(network_true[8:16],2)
Ctrue = int(network_true[16:24],2)
Dtrue = int(network_true[24:32],2)
Atrue_bin = network_true[0:8]
Btrue_bin = network_true[8:16]
Ctrue_bin = network_true[16:24]
Dtrue_bin = network_true[24:32]
mask_bin = '1'*int(mask)+'0'*(32-int(mask))
maskA = mask_bin[0:8]
maskB = mask_bin[8:16]
maskC = mask_bin[16:24]
maskD = mask_bin[24:32]
maskA_dec=int(maskA,2)
maskB_dec=int(maskB,2)
maskC_dec=int(maskC,2)
maskD_dec=int(maskD,2)
line1 = f'{Atrue:<8} {Btrue:<8} {Ctrue:<8} {Dtrue:<8}'
line2 = f'{Atrue_bin:<8} {Btrue_bin:<8} {Ctrue_bin:<8} {Dtrue_bin:<8}'
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
