import paho.mqtt.client as mqtt
import json


class MQTTClient:
    def __init__(self, host, token):
        self.host = host
        self.token = token
        self.client = mqtt.Client()
        self.client.username_pw_set(self.token)

    def connect(self):
        self.client.connect(self.host, 1883, 60)
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    def publish(self, topic, payload):
        self.client.publish(topic, json.dumps(payload))

    def subscribe(self, topic, callback):
        self.client.subscribe(topic)
        self.client.on_message = callback
