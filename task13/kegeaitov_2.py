from ipaddress import ip_network

net = ip_network('140.212.98.17/255.255.254.0', False)
print(net)
print(len(list(net.hosts())))
print(len(list(net)))