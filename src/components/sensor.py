import random
import time

class Sensor:
    def __init__(self, sensor_type):
        self.sensor_type = sensor_type

    def read_data(self):
        if self.sensor_type == 'temperature':
            return round(random.uniform(18, 35), 2)
        elif self.sensor_type == 'humidity':
            return round(random.uniform(30, 70), 2)
        elif self.sensor_type == 'soil_moisture':
            return round(random.uniform(10, 50), 2)
        else:
            raise ValueError("Unknown sensor type")

class TemperatureSensor(Sensor):
    def __init__(self):
        super().__init__('temperature')
        self.current_temp = random.uniform(18, 35)

    def read_data(self):
        delta = random.uniform(-0.5, 0.5)
        self.current_temp += delta
        self.current_temp = max(18, min(35, self.current_temp))
        return round(self.current_temp, 2)

class HumiditySensor(Sensor):
    def __init__(self):
        super().__init__('humidity')

class SoilMoistureSensor(Sensor):
    def __init__(self):
        super().__init__('soil_moisture')
