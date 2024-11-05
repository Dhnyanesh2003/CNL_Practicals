import socket


def dns_lookup():
    choice = input("Enter '1' for IP to URL lookup or '2' for URL to IP lookup: ")

    if choice == '1':
        # IP to URL lookup (Reverse DNS Lookup)
        ip_address = input("Enter IP address: ")
        try:
            url = socket.gethostbyaddr(ip_address)
            print(f"The domain name for IP {ip_address} is: {url[0]}")
        except socket.herror:
            print(f"Could not resolve IP {ip_address} to a URL.")

    elif choice == '2':
        # URL to IP lookup
        url = input("Enter URL: ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address for {url} is: {ip_address}")
        except socket.gaierror:
            print(f"Could not resolve URL {url} to an IP address.")

    else:
        print("Invalid choice. Please enter '1' or '2'.")


if __name__ == "__main__":
    dns_lookup()
