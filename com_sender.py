# sender_jetson.py
import socket
import json  


RECEIVER_IP = '192.168.0.102'
PORT = 5000

 


 


while True:
    
    geofence = input()

    data = json.dumps(geofence)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RECEIVER_IP, PORT))
        s.sendall(data.encode())
        print("Geofence data sent successfully!")
