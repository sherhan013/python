trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk','switchport trunk allowed vlan']
trunk = {'0/1': ['add', '10', '20'],'0/2': ['only', '11', '30'],'0/4': ['del', '17', '18']}
for intf, vlan_info in trunk.items():
    print ('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            print(f'{command}'+f'{vlan_info[0]}'.replace('del',' remove ').replace('only',' ').replace('add',' add ')+','.join(vlan_info[1:]))

        else:
            print(f'{command}')
