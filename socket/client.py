import socket
#1. creazione della sosket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

#2. connessione al server remoto 
remote_ip= '127.0.0.1'
remote_port= 8888

s.connect( (remote_ip,remote_port)  )

msg = input('>> ').strip()
while (msg != 'end'):
#3. invio messaggio
    s.sendall(msg.encode())
    msg = input('>> ').strip()

#4. Chiusura del socket
s.close()

