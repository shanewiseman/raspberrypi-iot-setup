import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("test/test")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.tls_set("/home/ubuntu/raspberrypi-iot-setup/paho-mqtt/certs.pem")
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("84e8a5b1-a766-470a-83bf-dbc79b1fa5ac", "wisemanss")
client.connect("mqtt.iot.shanedbwiseman.com", 8883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
