from typing import List
from .Device import Device, Items


class DeviceManager:
    def __init__(self):
        self.devices = []
    
    def add_device(self, device: Device):
        self.devices.append(device)
    
    def add_devices(self, devices: List[Device]):
        self.devices += devices
    
    def sort_by_price(self, reverse: bool = False, devices: List[Device] = None):
        return sorted(devices if devices else self.devices, key=lambda s: s.price, reverse=reverse)

    def sort_by_power(self, reverse: bool = False, devices: List[Device] = None):
        return sorted(devices if devices else self.devices, key=lambda s: s.power, reverse=reverse)

    def find_by_items(self, items_for_cake: Items):
        return [device for device in self.devices if device.get_type() == items_for_cake]
