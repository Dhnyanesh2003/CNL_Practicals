import socket

def Tcp_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server (localhost on port 12345)
    client_socket.connect(('localhost', 12346))

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024)
    print(f"Server Response: {response.decode()}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    Tcp_client()
