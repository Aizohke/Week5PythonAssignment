# Parent Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child Class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # Inheriting from Device
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        return f"Calling {number}  from {self.device_info()}"

    def charge(self):
        return f"{self.device_info()} is charging "

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}mAh"

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 15", 128, 4200)

# Test methods
print(phone1.phone_info())
print(phone2.make_call("+254700123456"))
print(phone1.charge())