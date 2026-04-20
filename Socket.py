import socket

HOST = ''  # Listen on all interfaces
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Got a request from {addr[0]}:{addr[1]}")

            request = conn.recv(1024)
            print("Request:")
            print(request.decode(errors='ignore'))

            # Basic routing
            if b"/health" in request:
                response_body = b"OK"
            else:
                response_body = b"Hello, World!"

            response = (
                b"HTTP/1.1 200 OK\r\n"
                b"Content-Type: text/plain\r\n"
                b"Content-Length: " + str(len(response_body)).encode() + b"\r\n"
                b"\r\n" +
                response_body
            )

            conn.sendall(response)
