import socket
import threading
import time

def start_tcp_server():
    # 1. Create a socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Bind to an address and port
    server_socket.bind(('127.0.0.1', 9999))
    
    # 3. Listen for incoming connections
    server_socket.listen(1)
    print("[TCP Server] Listening on 127.0.0.1:9999...")
    
    # 4. Accept a connection (This blocks until a client connects)
    client_socket, addr = server_socket.accept()
    print(f"[TCP Server] Connected by {addr}")
    
    # 5. Receive data
    data = client_socket.recv(1024)
    print(f"[TCP Server] Received: {data.decode('utf-8')}")
    
    # 6. Send response
    client_socket.send(b"ACK: Message Received!")
    
    # 7. Close connection
    client_socket.close()
    server_socket.close()
    print("[TCP Server] Connection closed.")

def start_tcp_client():
    time.sleep(1) # Wait for server to start
    
    # 1. Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Connect to the server (The 3-Way Handshake happens here!)
    print("[TCP Client] Connecting to server...")
    client_socket.connect(('127.0.0.1', 9999))
    
    # 3. Send data
    message = "Hello, TCP World!"
    print(f"[TCP Client] Sending: {message}")
    client_socket.send(message.encode('utf-8'))
    
    # 4. Receive response
    response = client_socket.recv(1024)
    print(f"[TCP Client] Response: {response.decode('utf-8')}")
    
    # 5. Close connection
    client_socket.close()

if __name__ == "__main__":
    # Run server in a separate thread so we can run client in the same script
    server_thread = threading.Thread(target=start_tcp_server)
    server_thread.start()
    
    start_tcp_client()
    server_thread.join()
