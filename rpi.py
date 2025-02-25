import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600)

while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').strip()
        distance = int(data)
        print(f"Distance: {distance} cm")
        
        if distance < 30:
            print("Distance is less than 30 cm, Servo should be OPEN.")
        else:
            print("Distance is more than 30 cm, Servo should be CLOSED.")
    
    time.sleep(1)
