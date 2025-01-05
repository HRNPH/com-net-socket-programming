import sys
from pathlib import Path
# Add the parent directory to the Python module search path
sys.path.append(str(Path(__file__).parent.parent))

# Import necessary libraries
import get_info
import json
import socket

def main():
    # TODO
    # Define the server host and port to connect to
    # Define your student-id
    
    # The function `extract()` from file `get_info.py` fetch computer's information and output in this format:
    # {
    #     "Hostname": <hostname>,
    #     "User": <current_user>,
    #     "OS": <os_system>,
    #     "OS version": <os_version>,
    #     "Mac": <mac>,
    #     "Local IP": <local_ip>,
    #     "Public IP": <public_ip>,
    # }
    # Keep OS info in message variable
    message = get_info.extract()
    
    # Add your student-ID to the message
    message["ID"] = ID
    
    # Now, the message should look like this:
    # {
    #     "ID": <id>
    #     "Hostname": <hostname>,
    #     "User": <current_user>,
    #     "OS": <os_system>,
    #     "OS version": <os_version>,
    #     "Mac": <mac>,
    #     "Local IP": <local_ip>,
    #     "Public IP": <public_ip>,
    # }

    try:
        # TODO
        # Create a socket object
        # =============================================


        # =============================================

        # TODO
        # Connect to the server
        # =============================================
        
        
        # =============================================
        print(f"[INFO] Connected to server at {server_host}:{server_port}")

        # TODO
        # After the connection has been established, send the information to the server
        # Use json.dumps() to convert the message to a string
        # Ensure the message is encoded in UTF-8 format before sending
        # =============================================


        # =============================================
        print(f"[INFO] Sent message: {message}")

        # TODO
        # Receive response from the server in json format {"TOKEN": <token>}
        # Use 1024 bytes as the buffer size
        # Ensure the response is decoded from UTF-8 format
        # =============================================
        
        
        # =============================================
        print(f"[INFO] Received response: {response.decode('utf-8')}")


    except ConnectionRefusedError:
        print("[ERROR] Could not connect to the server. Make sure it is running.")
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print("[INFO] Connection closed.")
        
if __name__ == '__main__':
    main()