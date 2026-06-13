import socket
import json

HOST = socket.gethostname() # gets host automatically 
PORT = 5555

CLIENT_NAME = "Client of Nina Abogadie and Gabrielle Marfil"   

def get_number():
    
    while True:
        try:
            num = int(
                input("Enter a number (1-100): ")
            )

            if 1 <= num <= 100:
                return num

            print("Number must be between 1 and 100.")

        except ValueError: # for NaN input 
            print("Invalid input. Enter an integer.")


def main():

    number = get_number()

    clientsocket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    print("CLIENT: Connecting...")

    # connect client to server 
    clientsocket.connect((HOST, PORT))

    print("CLIENT: Connected.")

    message = {
        "name": CLIENT_NAME,
        "number": number
    }

    clientsocket.send(
        json.dumps(message).encode()
    )

    print("CLIENT: Message sent.")

    data = clientsocket.recv(1024).decode()

    response = json.loads(data)

    server_name = response["name"]
    server_number = response["number"]

    print("\nCLIENT: Reply received.")

    print(f"Client Name: {CLIENT_NAME}")
    print(f"Server Name: {server_name}")

    print(f"Client Number: {number}")
    print(f"Server Number: {server_number}")

    print(f"Sum: {number + server_number}")

    clientsocket.close()

    print("CLIENT: Socket closed.")


if __name__ == "__main__":
    main()
