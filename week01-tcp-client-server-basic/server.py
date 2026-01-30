# server.py
import socket
from config import HOST, PORT, BUFFER_SIZE

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[SERVER] Listening on {HOST}:{PORT}")

#Step 4: Accept a Client Connection
conn, addr = server_socket.accept()
print(f"[SERVER] Connection from {addr}")
#________________________________________
#Step 5–6: Receive Data and Send Response
data = conn.recv(BUFFER_SIZE)
message = data.decode()
print(f"[SERVER] Received: {message}")

reply = f"ACK: {message}"
conn.sendall(reply.encode())
#________________________________________
#Step 7: Close the Connection
conn.close()
server_socket.close()
print("[SERVER] Closed connection")
