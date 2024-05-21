import socket

host = "127.0.0.1"
port = 55555


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    message = input("Введіть повідомлення (або 'exit' для завершення): ")
    client.sendall(message.encode())
    if message.lower() == 'exit':
        break
    data = client.recv(1024).decode()
    print(f"Відповідь від сервера: {data}")

client.close()


