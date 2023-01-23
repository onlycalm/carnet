import socket

RmtIpAdr = "127.0.0.1"
RmtPt = 9999

Socket = socket.socket()
Socket.connect((RmtIpAdr, RmtPt))

while True:
    RmtMsg = input("Client: ").strip()

    if not RmtMsg:
        continue

    Socket.sendall(RmtMsg.encode())

    if RmtMsg == "exit":
        print("Connect over.")
        break

    print("Server: ", Socket.recv(1024).decode())

Socket.close()
