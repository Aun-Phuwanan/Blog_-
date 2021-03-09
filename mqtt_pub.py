import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost")
client.publish("fobi/test","Hello FOBI")
#client.disconnect()
