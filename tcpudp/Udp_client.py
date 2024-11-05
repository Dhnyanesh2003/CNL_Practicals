import socket

def udp_client():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server address
    server_address = ('localhost', 12346)

    # Send a message to the server
    message = "Hello, UDP Server!"
    client_socket.sendto(message.encode(), server_address)

    # Receive response from the server
    response, server = client_socket.recvfrom(1024)
    print(f"Server Response: {response.decode()}")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    udp_client()
