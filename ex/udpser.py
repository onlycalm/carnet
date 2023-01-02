import socket

LocIpAddr = "127.0.0.1"
LocPt = 9999

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
Socket.bind((LocIpAddr, LocPt))

while True:
    CltMsg = Socket.recv(1024).decode()

    if CltMsg == "exit":
        exit("Connect over.")
    else:
        print("Client: ", CltMsg)

Socket.close()
