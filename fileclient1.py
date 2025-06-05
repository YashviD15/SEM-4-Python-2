import socket
host="192.168.104.121"
port=7777
client=socket.socket()

client.connect((host,port))
filename=r"C:\Users\LJENG\Desktop\text"
client.send(filename.encode())
f1=open(filename,"rb")
data=f1.read(1024)
while True:
    client.send(data)
    data=f.read(1024)
print("file sent")
client.close()
