import smbus2
import time
import math
from datetime import datetime, timezone
import requests

# MPU6050 Registers and Address
MPU6050_ADDR = 0x68
PWR_MGMT_1   = 0x6B
ACCEL_XOUT_H = 0x3B

# Initialize I2C
bus = smbus2.SMBus(1)

url = "http://100.72.88.113:8000/API/receive_message/"
# Attempt to wake up MPU6050 with error handling
def init_sensor():
    try:
        bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)
        return True
    except Exception as e:
        print("⚠️ MPU6050 not connected:", e)
        return False

def read_word_2c(addr):
    high = bus.read_byte_data(MPU6050_ADDR, addr)
    low = bus.read_byte_data(MPU6050_ADDR, addr+1)
    value = (high << 8) + low
    if value >= 0x8000:
        return -((65535 - value) + 1)
    else:
        return value

def get_accel_data():
    ax = read_word_2c(ACCEL_XOUT_H)
    ay = read_word_2c(ACCEL_XOUT_H + 2)
    az = read_word_2c(ACCEL_XOUT_H + 4)
    ax /= 16384.0
    ay /= 16384.0
    az /= 16384.0
    return ax, ay, az

def detect_fall(ax, ay, az, threshold=2.5):
    magnitude = math.sqrt(ax**2 + ay**2 + az**2)
    print(f"Accel Magnitude: {magnitude:.2f}g")
    return magnitude > threshold

# Main loop
print("Starting fall detection...")
while True:
    if init_sensor():
        try:
            ax, ay, az = get_accel_data()
            if detect_fall(ax, ay, az):
                print("🚨 Fall detected!")
                fall_data = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "has_fallen": True  
                }           
                response = requests.post(url, json=fall_data)
                time.sleep(2)
        except Exception as e:
            print("⚠️ Failed to read sensor data:", e)
    else:
        print("Retrying connection in 1 second...")

    time.sleep(0.05)
