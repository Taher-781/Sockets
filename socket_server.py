import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()
print("Waiting for connection")
connection_socket, address = server_socket.accept()
print("Client connected")
message = "Hello, thanks for connecting"
data = message.encode()
connection_socket.send(data)
connection_socket.close()
server_socket.close()