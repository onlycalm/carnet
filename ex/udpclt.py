import socket

RmtIpAddr = "127.0.0.1"
RmtPt = 9999

Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    RmtMsg = input("Client: ").strip()

    if not RmtMsg:
        continue

    Socket.sendto(RmtMsg.encode(), (RmtIpAddr, RmtPt))

    if RmtMsg == "exit":
        print("Connect over.")
        break

Socket.close()
