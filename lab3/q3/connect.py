import asyncio 
import socket

async def create_connection():

    #Create a socket object

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set the server address (127,0.8.1 and port 80)

    server_address = ('127.0.0.1', 2004)

    print(f"Connecting to server at {server_address}")

    # Connect to the server 
    await loop.sock_connect(client_socket, server_address) 
    print("Connection established")

    return client_socket

async def handle_connection(connection_id): 

    connection = await create_connection()

    # Perform actions with the connection If needed 
    print(f"Handling connection {connection_id}")

    # Note: Do not close the connection here

def main():

    num_connections = 50 # You can change this to the desired number of connections

    # Create the event Loop

    global loop

    loop=asyncio.get_event_loop()

    # Create tasks for creating connections

    connection_tasks = [handle_connection(i+1) for i in range(num_connections)]

    # Run the event loop until all tasks are done

    loop.run_until_complete(asyncio.gather(*connection_tasks))

    # Close the event toop

    loop.close()

if __name__ == "__main__":
    main()