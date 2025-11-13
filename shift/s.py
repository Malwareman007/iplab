import socket
def shift_cipher(text, key):
 result = ''
 for char in text:
 if char.isalpha():
 base = ord('A') if char.isupper() else ord('a')
 result += chr((ord(char) - base + key) % 26 + base)
 else:
 result += char
 return result
print("[1] Creating TCP socket for server...")
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[2] Binding socket to localhost:12345 ...")
server_socket.bind(('localhost', 12345))
print("[3] Starting to listen for client connections...")
server_socket.listen(1)
print("[✔] Server is ready and waiting for connections.\n")
conn, addr = server_socket.accept()
print(f"[4] Connection established with client {addr}")
print("[5] Waiting to receive data from client...")
data = conn.recv(1024).decode()
print(f"[6] Raw data received from client: {data}")
plaintext, key = data.split(',')
key = int(key)
print(f"[7] Extracted plaintext: '{plaintext}' and key: {key}")
print("[8] Encrypting message using Shift Cipher...")
ciphertext = shift_cipher(plaintext, key)
print(f"[9] Encrypted text: {ciphertext}")
print("[10] Sending encrypted text back to client...")
conn.send(ciphertext.encode())
print("[✔] Ciphertext sent successfully!\n")
print("[11] Closing connection...")
conn.close()
server_socket.close()
print("[✔] Server shut down successfully.")
