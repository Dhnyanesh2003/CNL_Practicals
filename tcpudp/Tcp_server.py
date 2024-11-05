import socket


def Tcp_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a local address and port
    server_socket.bind(('localhost', 12346))

    # Listen for incoming connections (max 5 connections in the queue)
    server_socket.listen(5)
    print("Server listening on port 12346...")

    while True:
        # Accept an incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        # Receive the data from the client
        data = client_socket.recv(1024)  # Buffer size is 1024 bytes
        print(f"Received data: {data.decode()}")

        # Send a response to the client
        response = "Message received"
        client_socket.send(response.encode())

        # Close the client connection
        client_socket.close()


if __name__ == "__main__":
    Tcp_server()
