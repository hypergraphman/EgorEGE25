from ipaddress import ip_network
net = ip_network('145.92.137.88/255.255.240.0', False)
print(net)