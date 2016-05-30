def ip_to_int32(ip):
    return sum([(int(octet) << 8*i)
               for i, octet in enumerate(ip.split('.')[::-1])])


print ip_to_int32("128.114.17.104") == 2154959208
print ip_to_int32("0.0.0.0") == 0
print ip_to_int32("128.32.10.1") == 2149583361
