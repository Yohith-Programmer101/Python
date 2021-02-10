import socket

s = socket.socket()
host = "192.168.1.35"
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Got connection from" , addr)
    c.send(b"Thankyou for connecting")
    c.close()
    