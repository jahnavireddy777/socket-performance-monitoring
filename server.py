import json
import socket

def start_server():
    # 1. Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind the socket to the address and port
    server_address = ('10.12.68.175', 8080)  # Replace with your server IP and desired port
    server_socket.bind(server_address)

    # 3. Server listens on all interfaces
    server_socket.listen(1)
    print(f"Server is listening on {server_address}")

    while True:
        # 4. Wait for an incoming connection
        client_socket, client_address = server_socket.accept()
        try:
            print(f"Connection received from {client_address}")

            # 5. Receive data from the client
            data = client_socket.recv(1024).decode()
            if not data:
                continue

            print(f"Data received: {data}")

            # 6. Try converting data from JSON, otherwise treat as plain text
            try:
                received_data = json.loads(data)
                is_json = True
            except json.JSONDecodeError:
                received_data = data
                is_json = False

            # 7. Process the registration and stock data
            if is_json:
                # If JSON received, you can implement custom logic
                response = {"status": "OK", "message": "JSON received", "data": received_data}
            else:
                # If plain text received (like "Request for stock prices")
                if "stock" in received_data.lower():
                    response = "Here are the stock prices: AAPL: $180, MSFT: $325, GOOGL: $150"
                else:
                    response = "Invalid request"

            # 8. Send response back to the client
            if is_json:
                client_socket.sendall(json.dumps(response).encode())
            else:
                client_socket.sendall(response.encode())

        finally:
            # 9. Close the client connection
            client_socket.close()
            print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    start_server()
