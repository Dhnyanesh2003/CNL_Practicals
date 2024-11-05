import socket

def udp_client(file_path):
    # Set up the UDP client to send data to the server at localhost:12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12348)

    # Send the filename to the server first
    filename = file_path.split("\\")[-1]  # Get only the file name from the full path
    client_socket.sendto(filename.encode(), server_address)

    # Open the file to send
    with open(file_path, 'rb') as f:
        print(f"Sending the file {filename}...")
        while True:
            # Read file in chunks of 1024 bytes
            file_data = f.read(1024)
            if not file_data:
                break  # End of file reached
            client_socket.sendto(file_data, server_address)  # Send each chunk to the server

    # Notify the server that file transmission is complete by sending an empty byte
    client_socket.sendto(b'', server_address)  # Sending an empty packet signifies end of transmission
    print(f"File '{filename}' sent successfully!")

    client_socket.close()

if __name__ == "__main__":
    # Specify the full path to the file to send
    file_path = r'C:\Users\LENOVO\Downloads\file_to_send.txt'  # Update the file path here
    udp_client(file_path)
