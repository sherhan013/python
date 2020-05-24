f = open('c:/ospf.txt', 'r')
for line in f:
    print ('Protocol: ' f'{line.split()[0]}'.replace('O','OSPF'))
    print ('Prefix: ' f'{line.split()[1]}')
    print ('AD/Metric: ' f'{line.split()[2]}'.strip('[]'))
    print ('Next hop: ' f'{line.split()[4]}'.strip(','))
    print ('Last update: ' f'{line.split()[5]}'.strip(','))
    print ('Outbound interface: ' f'{line.split()[6]}')
