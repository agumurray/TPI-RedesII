import socket

def udp_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))

    print(f"servidor UDP Echo comienza a escuchar en {host}:{port}")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"mensaje de {addr}: {data.decode()}")

        sock.sendto(data, addr)

server_ip = "0.0.0.0"  # escucha todas las interfaces
server_port = 7         # puerto UDP Echo

udp_server(server_ip, server_port)
