import tkinter as tk
import socket
import json

# Define receiver's IP and port
RECEIVER_IP = '192.168.0.101'  # Replace with your RPi's IP
PORT = 5000

# Function to send data over socket
def send_geofence(command):
    data = json.dumps(command)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((RECEIVER_IP, PORT))
        s.sendall(data.encode())
        print(f"Command '{command}' sent successfully!")
        print(type(command))
# Function to handle "Arm" button press
def arm():
    send_geofence("arm")

# Function to handle "Disarm" button press
def disarm():
    send_geofence("disarm")

# Set up the main GUI window
root = tk.Tk()
root.title("Geofence Controller")

# Set up buttons for "Arm" and "Disarm"
arm_button = tk.Button(root, text="Arm", width=20, height=2, command=arm)
arm_button.pack(pady=10)

disarm_button = tk.Button(root, text="Disarm", width=20, height=2, command=disarm)
disarm_button.pack(pady=10)

# Run the GUI main loop
root.mainloop()

