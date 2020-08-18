# Finding IP address by python

import socket

def getHostName_IP():
    try:
        hostName = socket.gethostname()
        hostIP = socket.gethostbyname(hostName)
        print("Hostname: ", hostName)
        print("IP: ", hostIP)    
    except:
        print("Unable to get Hostname & IP")

getHostName_IP()