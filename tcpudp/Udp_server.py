import socket

def udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a local address and port
    server_socket.bind(('localhost', 12346))
    print("UDP Server listening on port 12346...")

    while True:
        # Receive message from client
        message, client_address = server_socket.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Received message: {message.decode()} from {client_address}")

        # Send a response to the client
        response = "Message received"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    udp_server()
