import paho.mqtt.client as mqtt
import time

# Simulation of reading data from Modbus/RS485
def read_sensor_data():
    return {"temp": 42.5, "vibration": 0.02}

def on_connect(client, userdata, flags, rc):
    print("Connected to Broker")

client = mqtt.Client()
client.on_connect = on_connect
client.connect("localhost", 1883, 60)

while True:
    data = read_sensor_data()
    client.publish("factory/machine1/telemetry", str(data))
    time.sleep(5)
