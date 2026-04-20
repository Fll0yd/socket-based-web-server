import socket
import datetime

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

            # Parse request line
            request_line = request.split(b"\r\n")[0]
            print("Request line:", request_line)

            # Extract path
            try:
                path = request_line.split(b" ")[1]
            except IndexError:
                path = b"/"

            # Routing
            if path == b"/health":
                response_body = b"OK"
            elif path == b"/time":
                response_body = str(datetime.datetime.now()).encode()
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
