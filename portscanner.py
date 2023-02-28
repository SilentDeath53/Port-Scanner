import socket
import sys

target = input("Target IP address or domain name")

ports = range(1, 100)

# Use socket.SOCK_DGRAM insead of SOCK_STREAM for UDP ports
for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con = s.connect((target, port))
        print(f"Port {port} açık")
        con.close()
    except:
        pass
