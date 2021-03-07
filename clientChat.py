import socket
# from tkinter import *
# root = Tk()
# root.geometry("500x500")
# root.title("Chat Application")
# f1 = Frame(root, bg = "pink")
c = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
port = 12456
address = (ip, port)

c.connect(address)

while 1:
    msgFrom = c.recv(1024).decode()
    print("Server> ", msgFrom)
    # label = Label(f1, text = msgFrom)
    # msgValue = StringVar()
    msgTo = input("client> ")
    # msgTo.grid(row = 2, coloumn = 2)
    # Button(text = "submit", command = getValues).grid()
    c.send(bytes(msgTo, "utf-8"))
    
# root.mainloop()
c.close()