import socket
# import sys

s = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
port = 12456
address = (ip, port)

s.bind(address)
s.listen(2)
con, add = s.accept()
while 1:
    msgFrom = input("Server> ")
    con.send(bytes(msgFrom, "utf-8"))
    messageTo = con.recv(1024).decode()
    print("Client> ", messageTo)
