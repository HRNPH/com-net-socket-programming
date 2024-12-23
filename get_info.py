import os
import platform
import socket
import getpass
import requests
import netifaces

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
    net_if = netifaces.gateways()['default']
    net_if_name = list(net_if.values())[0][1]
    addrs = netifaces.ifaddresses(net_if_name)
    mac = addrs[netifaces.AF_LINK][0]['addr']

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
