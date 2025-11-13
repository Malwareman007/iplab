import socket, threading

def encrypt(msg, key):
    return ''.join(chr((ord(c)+key)%256) for c in msg)

def decrypt(msg, key):
    return ''.join(chr((ord(c)-key)%256) for c in msg)

key = int(input("Enter key (3 for C1, 5 for C2): "))
s = socket.socket()
s.connect(('localhost',12345))
print(s.recv(1024).decode())

def rec():
    while True:
        try:
            d = s.recv(1024).decode()
            if d:
                print("\nEncrypted:",d)
                print("Decrypted:",decrypt(d,key))
        except:
            break

threading.Thread(target=rec,daemon=True).start()

while True:
    msg=input()
    if msg=="exit": break
    s.send(encrypt(msg,key).encode())

s.close()
