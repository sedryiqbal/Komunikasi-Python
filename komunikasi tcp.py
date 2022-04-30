import socket

#create socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#define ip address and port
IPADDR = '192.168.100.30'
PORT = 28097
ADDR = (IPADDR,PORT)

#bind
s.bind(ADDR)

while True:
#allow 5 simultaneous
    s.listen(5)

#accepting new connection
    conn, addr = s.accept()

#receive data
    data = conn.recv(1024)
    d = data.decode('utf-8')
    print (d)

#send data
    s.send(str(d).encode('utf-8'))
    print("Data Terkirim")

#close socket
conn.close()
s.close()

