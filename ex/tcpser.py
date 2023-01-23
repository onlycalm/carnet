import socket

LocIpAdr = "127.0.0.1"
LocPt = 9999

Socket = socket.socket()
Socket.bind((LocIpAdr, LocPt))
Socket.listen(5)
print("Server: listening.")
Conn, RmtIpAdr = Socket.accept()

while True:
    CltMsg = Conn.recv(1024).decode()

    if CltMsg == "exit":
        exit("Connect over.")
    else:
        print("Client: ", CltMsg)
        Conn.sendall(CltMsg.encode())
        print("Server: ", CltMsg)

Conn.close()
