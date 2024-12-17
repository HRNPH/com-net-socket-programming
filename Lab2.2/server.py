import socket, json
from pyngrok import ngrok

def main():
    host = ""
    # TODO
    # Specify your desired port
    # =============================================
    
    
    # =============================================
    is_running = True

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # TODO
            # Complete the following block
            # =============================================
            
            
            # =============================================
            s.settimeout(1.0)
            print(f"[INFO] Server started, listening on port {port}")
            
            # Expose the server using ngrok
            public_url = ngrok.connect(port, "tcp")
            print(f"[INFO] Server is accessible via public URL: {public_url}")
            
            while is_running:
                try:
                    # TODO
                    # Got a connection from a client
                    # =============================================
                    
                    
                    # =============================================
                    print(f"[INFO] Connection accepted from {client_address}")
                    
                    with client_socket:
                        print(f"[INFO] Connected to: {client_address[0]}:{client_address[1]}")
                        
                        # TODO
                        # Receive a message from the socket, "Hello World!"
                        # =============================================
                        
                        
                        # =============================================
                        print("[INFO] Received message:", data)
                        
                        # TODO
                        # Respond "OK" to the client
                        # =============================================
                        
                        
                        # =============================================
                        print(f"[INFO] Responded to Client {client_address[0]}:{client_address[1]}.")
                        print(f"[INFO] Client {client_address[0]}:{client_address[1]} disconnected.")
    
                except socket.timeout:
                    continue

    except KeyboardInterrupt:
        print("[INFO] Received shutdown signal (Ctrl+C). Stopping server...")
        is_running = False
    except Exception as e:
        print(f"[ERROR] Exception in server loop: {e}")
        
    print("[INFO] Server shutdown complete.")
            
if __name__ == '__main__':
    main()
