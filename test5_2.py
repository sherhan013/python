input_data = input('Введите ip-адрес сети в формате x.x.x.x/m: ')
network = input_data.split('/')[0]
octets = network.split('.')
A = octets[0]
B = octets[1]
C = octets[2]
D = octets[3]
Abin = '{:08b}'.format(int(A))
Bbin = '{:08b}'.format(int(B))
Cbin = '{:08b}'.format(int(C))
Dbin = '{:08b}'.format(int(D))
mask = input_data.split('/')[1]
mask_bin = '1'*int(mask)+'0'*(32-int(mask))
mask_bin_list = list(mask_bin)
maskA = ''.join(mask_bin_list[:8])
maskB = ''.join(mask_bin_list[8:16])
maskC = ''.join(mask_bin_list[16:24])
maskD = ''.join(mask_bin_list[24:32])
maskA_dec=int(maskA,2)
maskB_dec=int(maskB,2)
maskC_dec=int(maskC,2)
maskD_dec=int(maskD,2)
line1 = '{:<9}'.format(A)+'{:<9}'.format(B)+'{:<9}'.format(C)+'{:<9}'.format(D)
line2 = '{:<8}'.format(Abin)+' '+'{:<8}'.format(Bbin)+' '+'{:<8}'.format(Cbin)+' '+'{:<8}'.format(Dbin)
line3 = '{:<9}'.format(maskA_dec)+'{:<9}'.format(maskB_dec)+'{:<9}'.format(maskC_dec)+'{:<9}'.format(maskD_dec)
line4 = '{:<8}'.format(maskA)+' '+'{:<8}'.format(maskB)+' '+'{:<8}'.format(maskC)+' '+'{:<8}'.format(maskD)




print('Network:')
print(line1)
print(line2)
print(' ')
print('Mask: ')
print(line3)
print(line4)

input()
