import socket
import threading

def client_handler(connection, otherclient):
    while True:
        try:
            # Receive message from one client
            message = connection.recv(1024).decode()
            print(f"Received message: {message}")
            # Forward message to the other client
            if otherclient:
                otherclient.send(message.encode())
        except:
            # An error occurred, break the loop
            print("An error occurred!")
            break

def main():
    host = '127.0.0.1'  
    port = 8000        

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server is listening on {host}:{port}")

    clients = []
    conn1, addr1 = server_socket.accept()
    print(f"Connected to {addr1}")
    clients.append(conn1)
    conn1.send("first".encode())
    conn2, addr2 = server_socket.accept()
    print(f"Connected to {addr2}")
    clients.append(conn2)
    conn2.send("second".encode())
    threading.Thread(target=client_handler, args=(conn1, conn2)).start()
    threading.Thread(target=client_handler, args=(conn2, conn1)).start()

    print("Both clients are connected, ready to play.")


if __name__ == "__main__":
    main()