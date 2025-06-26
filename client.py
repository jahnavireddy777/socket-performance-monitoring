# client.py
import socket

def connect_to_server():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server with the given IP and port
    server_address = ('10.12.68.175', 8080)
    client_socket.connect(server_address)
    
    try:
        # Send stock request data
        stock_request = "Request for stock prices"
        client_socket.sendall(stock_request.encode())
        
        # Receive response from the server
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")
        
    finally:
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    connect_to_server()
