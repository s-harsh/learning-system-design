import socket

def dns_lookup(domain):
    print(f"\n--- 1. DNS Lookup for {domain} ---")
    try:
        # Get the IP address for the domain
        ip_address = socket.gethostbyname(domain)
        print(f"Domain: {domain}")
        print(f"IP Address: {ip_address}")
        print("Note: This is the address your computer will connect to.")
        return ip_address
    except socket.gaierror:
        print(f"Error: Could not resolve {domain}")
        return None

def raw_http_request(domain, ip):
    print(f"\n--- 2. Raw HTTP Request to {domain} ---")
    port = 80 # Standard HTTP port
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        print(f"Connecting to {ip}:{port}...")
        client_socket.connect((ip, port))
        
        # Construct a raw HTTP GET request
        # \r\n is the standard line ending for HTTP
        request = f"GET / HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\n\r\n"
        print("Sending Request:")
        print(request)
        
        # Send the request
        client_socket.send(request.encode('utf-8'))
        
        # Receive the response
        response = b""
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break
            response += chunk
            
        print("Received Response (First 500 characters):")
        print("-" * 40)
        print(response.decode('utf-8', errors='ignore')[:500])
        print("-" * 40)
        print("... (truncated)")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    target_domain = "example.com"
    target_ip = dns_lookup(target_domain)
    
    if target_ip:
        raw_http_request(target_domain, target_ip)
