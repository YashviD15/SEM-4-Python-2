import socket
host=socket.gethostname()
port=5000
client=socket.socket()
client.connect((host,port))
msg=input("Enter ypur msg: ")
while msg!="bye":
    client.send(msg.encode())
    data=client.recv(1024).decode()
    print("Recieved msg: ",str(data))
    msg=input("Enter your msg: ")
client.close()
    
