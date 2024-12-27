import os
import getmac
import socket
import getpass
import requests
import platform

def extract():
    # Get Hostname
    hostname = socket.gethostname()

    # Get Current User
    current_user = getpass.getuser()

    # Get OS Information
    os_system = platform.system()  # e.g., Windows, Linux, Darwin (macOS)
    os_version = platform.version()  # OS version

    # Get Local IP Address
    local_ip = socket.gethostbyname(socket.gethostname())

    # Get Public IP Address
    try:
        public_ip = requests.get("https://api.ipify.org").text
    except Exception as e:
        public_ip = ""
        
    # Get MAC Address
    mac = getmac.get_mac_address()

    info = {
        "Hostname": hostname,
        "User": current_user,
        "OS": os_system,
        "OS version": os_version,
        "Mac": mac,
        "Local IP": local_ip,
        "Public IP": public_ip,
    }
    
    return info
