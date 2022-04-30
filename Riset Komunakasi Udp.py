#!/usr/bin/env python
import socket
import serial   

#arduino = serial.Serial('COM18', 500000,timeout=.1) #Untuk komunikasi ke arduino
#menentukan ip address dan port
IPADDR = '192.168.100.30'
PORT = 28097
ADDR = (IPADDR,PORT)

#membuat socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#bind
s.bind(ADDR)

while True:
    data, addr = s.recvfrom(1024)
    d = data.decode('utf-8')
    print (d) # anda dapat mengkonversi byte string ke string Unicode menggunakan  s.decode('utf-8')
    print ("MASOOOOOOOOOOOOOOOOOK")
    #arduino.write(str(data).encode('utf-8'))
    #arduino.write('d'.encode('utf-8'))
    #print (addr)
    
#menutup socket
s.close()
