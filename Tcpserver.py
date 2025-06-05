import socket
host=""
port=5000
server=socket.socket()
server.bind((host,port))
server.listen()
conn,add=server.accept()
while True:
    data=conn.recv(1024).decode()
    if data=="bye":
        break
    print("Msg recieved :",str(data))
    data=input("Enter Your Msg to send:")
    conn.send(data.encode())
conn.close()
