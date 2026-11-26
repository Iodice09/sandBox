import socket 

#1. creazione della socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#2. binding ->  associare la socket all'indirizzo ip e alla porta 
local_host = ""
local_port = 8888 
#qua effettivamente prende le variabili e le mette nel bind
s.bind(  (local_host, local_port)   )
print(f'socket creata e associata a 127.0.0.1:{local_port}')

#3. ascolto (listen)
s.listen ( 10 )
print('Socket in ascolto')

# 4. accettare la connessione 
print ('attesa.....')
conn, addr = s.accept()
ip_remote= addr[0]
port_remote = str(addr[1])
print(f'connessione da {ip_remote}: {port_remote}')

#5. ricezione del messaggio
while True :
    msg = conn.recv(4096).strip().decode() #per decodificare e eliminare eventuali spazi
    if msg == 'end' :
        break
    print (msg)

#6. chiusura delle socket
conn.close()
s.close()
