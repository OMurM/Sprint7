class Actuator:
    def __init__(self, actuator_type):
        self.actuator_type = actuator_type

    def activate(self):
        """Simulate actuator activation"""
        print(f"Activating {self.actuator_type}.")

    def deactivate(self):
        """Simulate actuator deactivation"""
        print(f"Deactivating {self.actuator_type}.")

class WaterPump(Actuator):
    def __init__(self):
        super().__init__('water pump')

class Fan(Actuator):
    def __init__(self):
        super().__init__('fan')
