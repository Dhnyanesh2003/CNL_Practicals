import socket

def udp_server():
    # Set up the UDP server to listen on port 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12348))  # Listening on localhost and port 12345
    print("Server is listening for incoming file transfer on port 12345...")

    # Receive the filename from the client first
    filename, client_address = server_socket.recvfrom(1024)  # Receive the filename first
    filename = filename.decode()  # Decode the filename

    # Open the file to write the received data
    with open(f"received_{filename}", 'wb') as f:
        print(f"Receiving the file {filename}...")
        while True:
            # Receive file data from the client in 1024-byte chunks
            data, _ = server_socket.recvfrom(1024)
            if not data:  # No data means the client has finished sending
                break
            f.write(data)  # Write data to the file

    print(f"File '{filename}' received successfully!")
    server_socket.close()

if __name__ == "__main__":
    udp_server()
