import socket as s
print("Hostname: ", s.gethostname())
print("Host: ", s.gethostbyname(s.gethostname()))