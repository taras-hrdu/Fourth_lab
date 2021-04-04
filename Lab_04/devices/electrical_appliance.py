from .Device import Device, Items


class ElectricalAppliance(Device):
    def __init__(self, items_for_cake: Items, brand: str = "", price: int = 0, name: str = "",  weight_in_kg: int = 0,
                 color: str = "", power: int = 0, guarantee: float = 0, energy_consumption: float = 0,
                 cord_length: float = 0, number_of_buttons: int = 0):
        super().__init__(Items.Not_involved, brand, price, name, weight_in_kg, color, power, guarantee)
        self.energy_consumption = energy_consumption
        self.cord_length = cord_length
        self.number_of_buttons = number_of_buttons
