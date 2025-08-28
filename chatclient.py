import socket
import threading

def empfangen(client_socket):
    while True:
        try:
            nachricht = client_socket.recv(1024).decode('utf-8')
            if not nachricht:
                break
            print(nachricht)
        except:
            print("Verbindung zum Server verloren.")
            break

def senden(client_socket, username):
    while True:
        nachricht = input()
        if nachricht == '!quit':
            client_socket.close()
            break
        nachricht_mit_username = f"{username}: {nachricht}"
        print(nachricht_mit_username)
        client_socket.send(nachricht_mit_username.encode('utf-8'))

def main():
    HOST = input("Bitte gib die Server-IP-Adresse ein: ")
    PORT = int(input("Bitte gib den Server-Port ein: "))
    username = input("Bitte gib deinen Benutzernamen ein: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
        print(f"Verbunden mit dem Server unter {HOST}:{PORT}")
    except socket.error as e:
        print(f"Verbindungsfehler: {e}")
        return

    # Threads für Senden und Empfangen erstellen
    empfangs_thread = threading.Thread(target=empfangen, args=(client,))
    sende_thread = threading.Thread(target=senden, args=(client, username))

    # Threads starten
    empfangs_thread.start()
    sende_thread.start()

if __name__ == "__main__":
    main()