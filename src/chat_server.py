import socket, threading
from chatbot import bot_reply

HOST = '127.0.0.1'
PORT = 65432

def handle_client(conn, addr):
    user_id = 1  # demo only
    conn.sendall(b"Welcome to MHJ chatbot. Type 'bye' to exit.\n")
    while True:
        msg = conn.recv(1024).decode().strip()
        if not msg or msg.lower() == 'bye':
            break
        reply = bot_reply(user_id, msg)
        conn.sendall(reply.encode()+b"\n")
    conn.close()

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Chat server running...")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    start_server()
