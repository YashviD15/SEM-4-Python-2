import socket
host=""
port=7777
server=socket.socket()
server.bind((host,port))
server.listen()
conn,add=server.accept()
filename=conn.recv(1024).decode()

f=open(filename,"wb")
while True:
    data=conn.recv(1024)
    if not data:
        break
    f.write(data)
print("recievd sucees")
conn.close()

