import socket

def tcp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12347))

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())

    # Receive and print the response from the server
    response = client_socket.recv(1024).decode()
    print(f"Server says: {response}")

    # Open the file to send
    with open(r'C:\Users\LENOVO\Downloads\file_to_send.txt', 'rb') as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)

    print("File sent successfully.")
    client_socket.close()

    client_socket.close()

if __name__ == "__main__":
    tcp_client()


