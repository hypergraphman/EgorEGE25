from ipaddress import ip_network

net = ip_network('131.72.131.45/255.255.255.192', False)
k = 0
for ad in net:
    if f'{int(ad):b}'.count('1') % 2 != 0:
        k += 1
print(k)