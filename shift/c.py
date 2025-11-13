import socket
print("[1] Creating TCP socket for client...")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[2] Connecting to server at localhost:12345 ...")
client_socket.connect(('localhost', 12345))
print("[✔] Connection established with server.\n")
plaintext = input("Enter message to encrypt: ")
key = int(input("Enter shift key: "))
print(f"[3] Preparing data to send -> Plaintext: '{plaintext}', Key:
{key}")
data = f"{plaintext},{key}"
print(f"[4] Sending data to server: {data}")
client_socket.send(data.encode())
print("[5] Waiting for server response...")
ciphertext = client_socket.recv(1024).decode()
print(f"[6] Received encrypted message from server: {ciphertext}")
print("[7] Closing connection with server...")
client_socket.close()
print("[✔] Client finished successfully.")
