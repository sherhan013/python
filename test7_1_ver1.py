f = open('c:/ospf.txt', 'r')
for line in f:
    print (f'''
    Protocol: {line.split()[0].replace('O','OSPF')}
    Prefix:  {line.split()[1]}
    AD/Metric: {line.split()[2].strip('[]')}
    Next hop:  {line.split()[4].strip(',')}
    Last update: {line.split()[5].strip(',')}
    Outbound interface: {line.split()[6]}
    ''')
