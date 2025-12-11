import socket
import time 

def tcp_client(host, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Conectado a {host}:{port}")
        client_socket.sendall(message.encode())
        if port == 7: 
            response = client_socket.recv(1024)
            print(f"Respuesta: {response.decode()}")
        print("Conexión cerrada")

HOST = "140.222.20.2" 
PORT_DISCARD = 9
PORT_ECHO = 7

tcp_client(HOST, PORT_DISCARD, "Prueba discard")

time.sleep(1)

tcp_client(HOST, PORT_ECHO, "Prueba echo")
