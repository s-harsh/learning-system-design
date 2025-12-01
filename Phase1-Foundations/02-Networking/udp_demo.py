import socket
import threading
import time

def start_udp_server():
    # 1. Create a socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. Bind to an address and port
    server_socket.bind(('127.0.0.1', 9999))
    print("[UDP Server] Listening on 127.0.0.1:9999...")
    
    # 3. Receive data (No "accept" needed! No connection!)
    data, addr = server_socket.recvfrom(1024)
    print(f"[UDP Server] Received from {addr}: {data.decode('utf-8')}")
    
    # 4. Send response (Must specify address because there is no connection)
    server_socket.sendto(b"ACK: Message Received!", addr)
    
    server_socket.close()

def start_udp_client():
    time.sleep(1)
    
    # 1. Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. Send data (No "connect" needed!)
    message = "Hello, UDP World!"
    print(f"[UDP Client] Sending: {message}")
    client_socket.sendto(message.encode('utf-8'), ('127.0.0.1', 9999))
    
    # 3. Receive response
    response, addr = client_socket.recvfrom(1024)
    print(f"[UDP Client] Response: {response.decode('utf-8')}")
    
    client_socket.close()

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_udp_server)
    server_thread.start()
    
    start_udp_client()
    server_thread.join()
