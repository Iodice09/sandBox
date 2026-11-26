import socket
#1. creazione della sosket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM )

#2. connessione al server remoto 
remote_ip= '127.0.0.1'
remote_port= 8888

s.connect( (remote_ip,remote_port)  )

while True:
#3. invio messaggio
    msg = input('>> ').strip()
    s.sendall(msg.encode())
    if msg == 'end':
        break
    

#4. Chiusura del socket
s.close()

