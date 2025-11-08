import socket
import time

PI_IP = "172.20.10.3"  # Replace with your Pi’s IP
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((PI_IP, PORT))
    print("[Jetson] Connected to Raspberry Pi")

    while True:
        cmd = input("Enter command (on/off/exit): ").strip().lower()
        if cmd == "on":
            s.sendall(b"camera_on")
        elif cmd == "off":
            s.sendall(b"camera_off")
        elif cmd == "exit":
            s.sendall(b"exit")
            break
        else:
            print("Invalid command")
        time.sleep(1)