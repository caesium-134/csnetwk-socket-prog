import socket
import json 

HOST = socket.gethostname()
PORT = 5555 

SERVER_NAME = "Server of _____" # fill in later
SERVER_NUMBER = 50 

def main(): 

    # line 14-21 from python socket tutorial 

    # create an INET, STREAMing socket 
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # bind the socket to a public host, and a well-known port 
    serversocket.bind((HOST, PORT))
    
    # become a server socket
    serversocket.listen(5)

    print(f"SERVER: Listening on {HOST}:{PORT}")
    
    
    while True: 
        print("\nSERVER: Waiting for connection...") 

        # accept connections from outside 
        (clientsocket, address) = serversocket.accept() 

        print(f"SERVER: Connection from {address}") 

        data = clientsocket.recv(1024).decode() 

        message = json.loads(data)

        client_name = message["name"]
        client_number = message["number"]

        print(f"Client Name: {client_name}")
        print(f"Server Name: {SERVER_NAME}") 

        # shutdown condition 
        if client_number < 1 or client_number > 100: 
                
                print("SERVER: Out-of-range number received.")
                print("SERVER: Terminating.")

                clientsocket.close()
                serversocket.close()

                return 
        
        total = client_number + SERVER_NUMBER 

        print(f"Client Number: {client_number}")
        print(f"Server Number: {SERVER_NUMBER}") 
        print(f"Sum: {total}")

        response = {
            "name": SERVER_NAME, 
            "number": SERVER_NUMBER 
        }

        clientsocket.send(
            json.dumps(response).encode()
        )

        print("SERVER: Reply sent.")

        clientsocket.close()

        print("SERVER: Client disconnected.")

if __name__ == "__main__":
    main() 

