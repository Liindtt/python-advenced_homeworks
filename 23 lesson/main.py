import socket
from datetime import datetime
from time import sleep

host = "127.0.0.1"
port = 55555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()
print("Server running...")


while True:
    client, address = server_socket.accept()
    print(f"Connected with {address}")
    data = client.recv(1024).decode("utf-8")
    if not data or data.lower() == "exit":
        print("Клієнт завершив з'єднання")
        break
    print(f"Отримано: {data}")
    print(f"Час отримання: {datetime.now()}")
    sleep(5)
    sent = client.send(data.encode())
    if sent == len(data):
        print("Відповідь успішно відправлена")
    client.close()


