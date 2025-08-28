import requests
import time
import threading

SERVER_URL = 'http://192.168.88.98:5000'  # Ersetze <SERVER_IP> mit der IP-Adresse des Servers

def senden(username):
    while True:
        message = input()
        if message == '!quit':
            break
        data = {'username': username, 'message': message}
        try:
            response = requests.post(f'{SERVER_URL}/chat', data=data)
            if response.status_code != 200:
                print(f"Fehler beim Senden der Nachricht: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Verbindungsfehler: {e}")

def empfangen():
    while True:
        try:
            response = requests.get(f'{SERVER_URL}/messages')
            if response.status_code == 200:
                new_messages = response.json()
                for message in new_messages:
                    print(message)
            else:
                print(f"Fehler beim Empfangen von Nachrichten: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Verbindungsfehler: {e}")
        time.sleep(1)  # Warte 1 Sekunde, bevor erneut geprüft wird

def main():
    username = input("Bitte gib deinen Benutzernamen ein: ")

    sende_thread = threading.Thread(target=senden, args=(username,))
    empfangs_thread = threading.Thread(target=empfangen)

    sende_thread.start()
    empfangs_thread.start()

if __name__ == "__main__":
    main()