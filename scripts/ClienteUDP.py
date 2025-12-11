import socket

def udp_echo_client(server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "mensaje desde servidor UDP"
    print(f"enviando: {message}")
    sock.sendto(message.encode(), (server_ip, server_port))

    response, server = sock.recvfrom(1024)
    print(f"recibido: {response.decode()}")

    sock.close()

server_ip = "140.222.20.2"
server_port = 7              

udp_echo_client(server_ip, server_port)
