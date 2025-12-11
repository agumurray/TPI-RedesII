import socket

def tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"servidor TCP comienza a escuchar en {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"conexion recibida de {client_address}")

        while True:
            data = client_socket.recv(1024) 
            if not data: 
                break
        print(f"conexion cerrada por {client_address}")
        client_socket.close()

HOST = "0.0.0.0"
PORT = 9000

tcp_server(HOST, PORT)
