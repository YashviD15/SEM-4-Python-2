import socket
host="192.168.107.21"
port=8000
client=socket.socket(type=socket.SOCK_DGRAM)
while True:
    msg=input("enter msg")
    client.sendto(msg.encode(),(host,port))
    data,add=client.recvfrom(1024)
    print("recived",data,decode())
client.close()
