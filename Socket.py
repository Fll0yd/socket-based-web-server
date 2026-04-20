import socket

HOST = ''  # The IP address or hostname of your Raspberry Pi
PORT = 8080  # The port number you want to use for your web server

if b"/health" in request:
    response = b"HTTP/1.1 200 OK\r\n\r\nOK"
else:
    response = b"HTTP/1.1 200 OK\r\n\r\nHello, World!"
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Got a request from {addr[0]}:{addr[1]}")
            conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello, World!")
