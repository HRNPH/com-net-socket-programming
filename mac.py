import netifaces

def extract():
    # Get the default network interface
    default_if = netifaces.gateways()['default']
    default_if_name = list(default_if.values())[0][1]
    
    # Get the MAC Address (string)
    addrs = netifaces.ifaddresses(default_if_name)
    MAC = addrs[netifaces.AF_LINK][0]['addr']
    
    return MAC
    