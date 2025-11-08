import zmq
import time

def create_socket():
    context = zmq.Context()
    socket_push_jaw = context.socket(zmq.PUB)  
    socket_push_jaw.bind("tcp://localhost:5000")   
    return socket_push_jaw

def get_input(previous_value):
    try: 
        value_input = input(f"Enter value (press Enter to send default value {previous_value}): ")
        if value_input == "":  
            value = previous_value
        else:
            value = value_input   
        
    except ValueError:
        print("Invalid input. Please enter a string value.")
        return get_input(previous_value)   
    
    return value

def send_data(socket, value): 
    socket.send_string(value)   

def main():
    socket = create_socket()
    
    print("Testing script running. Enter values for data.")
    print("Type 'exit' to quit.") 
    
    previous_value = "3900"  

    while True:
        value = get_input(previous_value)
        
        if value == "exit":
            print("Exiting testing script.")
            break
        
        send_data(socket, value)
        print(f"Sent value: {value}")
        
        previous_value = value  # Update previous value
        
        
if __name__ == "__main__":
    main()
