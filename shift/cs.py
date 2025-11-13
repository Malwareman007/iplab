import socket, threading

def encrypt(msg, key):
    return ''.join(chr((ord(c)+key)%256) for c in msg)

def decrypt(msg, key):
    return ''.join(chr((ord(c)-key)%256) for c in msg)

server = socket.socket()
server.bind(('localhost',12345))
server.listen(2)
print("Server running...")

clients = {}
keys = {1:3, 2:5}

def handle(cid):
    conn = clients[cid]
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data: break
            msg = decrypt(data, keys[cid])
            print(f"Client{cid}:", msg)
            other = 2 if cid==1 else 1
            if other in clients:
                conn2 = clients[other]
                conn2.send(encrypt(msg, keys[other]).encode())
        except:
            break
    conn.close()
    print(f"Client{cid} left")

# accept both clients first
for i in [1,2]:
    c, a = server.accept()
    clients[i] = c
    c.send(f"You are Client{i}".encode())
    threading.Thread(target=handle, args=(i,), daemon=True).start()

print("Both clients connected. Chat active!")

# keep main thread alive forever
while True:
    pass
