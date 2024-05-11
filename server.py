import socket
import threading
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8000))
server.listen()

clients = []
positions = {}
turn = 1
snakes = {32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 97: 78}
ladders = {1: 38, 4: 14, 8: 30, 21: 42, 28: 76, 50: 67, 71: 92, 80: 99}

def send_positions():
    global clients, positions
    for client in clients:
        message = ','.join([f"{name}:{position}" for name, position in positions.items()])
        client.send(message.encode('utf-8'))

def handle(client):
    global positions, turn
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if not data:
                break
            if data == 'roll_dice':
                if turn == 1 and client == clients[0]:
                    roll = random.randint(1, 6)
                    positions['Player 1'] += roll
                    if positions['Player 1'] in snakes:
                        positions['Player 1'] = snakes[positions['Player 1']]
                    elif positions['Player 1'] in ladders:
                        positions['Player 1'] = ladders[positions['Player 1']]
                    turn = 2
                    send_positions()
                elif turn == 2 and client == clients[1]:
                    roll = random.randint(1, 6)
                    positions['Player 2'] += roll
                    if positions['Player 2'] in snakes:
                        positions['Player 2'] = snakes[positions['Player 2']]
                    elif positions['Player 2'] in ladders:
                        positions['Player 2'] = ladders[positions['Player 2']]
                    turn = 1
                    send_positions()
        except Exception as e:
            print(f"Error: {e}")
            break

def start_game():
    global positions
    positions = {'Player 1': 0, 'Player 2': 0}
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        clients.append(client)
        if len(clients) == 2:
            send_positions()
            thread = threading.Thread(target=handle, args=(clients[1],))
            thread.start()
            handle(clients[0])

start_game()
