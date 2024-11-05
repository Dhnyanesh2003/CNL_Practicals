import socket

def tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12347))
    server_socket.listen(1)
    print("Server listening on port 12345...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive and print the message from the client
    message = client_socket.recv(1024).decode()
    print(f"Client says: {message}")

    # Send a response to the client
    client_socket.send("Hello, Client!".encode())

    # Open a file to write the received data
    with open('received_file.txt', 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)

    print("File received successfully.")

    client_socket.close()

if __name__ == "__main__":
    tcp_server()





