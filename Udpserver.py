import socket
host=""
port=5000
server=socket.socket()
server.bind((host,port))
while True:
    print("Waiting for msg")
    conn,add=server.recvfrom(1024).decode()
    print(f"data recieved from {add} data is {conn.decode()}")
    msg=input("Enter Your Msg to send:")
    server.sendto(msg.encode(),add)
conn.close()
