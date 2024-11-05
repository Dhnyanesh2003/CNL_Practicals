def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 127:  # Class A
        return "Class A", "255.0.0.0"
    elif 128 <= first_octet <= 191:  # Class B
        return "Class B", "255.255.0.0"
    elif 192 <= first_octet <= 223:  # Class C
        return "Class C", "255.255.255.0"
    else:
        return "Unknown", "N/A"

def main():
    ip = input("Enter IP address (e.g., 192.168.1.1): ").strip()
    ip_class, subnet_mask = get_ip_class(ip)
    print(f"IP Address: {ip}")
    print(f"Class: {ip_class}")
    print(f"Subnet Mask: {subnet_mask}")

if __name__ == "__main__":
    main()
