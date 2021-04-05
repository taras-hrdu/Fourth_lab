from .electrical_appliance import ElectricalAppliance
from .Device import Items


class Kettle(ElectricalAppliance):
    def __init__(self, brand: str = "", price: int = 0, name: str = "", weight_in_kg: int = 0,  color: str = "",
                 power: int = 0, guarantee: float = 0, energy_consumption: float = 0, cord_length: float = 0,
                 number_of_buttons: int = 0, volume: int = 0, heating_element: str = ''):
        super().__init__(Items.Not_involved, brand, price, name, weight_in_kg, color, power, guarantee,
                         energy_consumption, cord_length, number_of_buttons)
        self.volume = volume
        self.heating_element = heating_element

    def __str__(self):
        res2 = f"brand: {self.brand}\nprice: {self.price}\nname: {self.name}\nitems_for_cake: {self._items_for_cake}\n"\
        f"weight: {self.weight_in_kg}\ncolor: {self.color}\npower: {self.power}\nguarantee: {self.guarantee}\n"\
        f"energy: {self.energy_consumption}\ncord: {self.cord_length}\nnumber_of_buttons: {self.number_of_buttons}\n"\
        f"volume: {self.volume}\nheating_element: {self.heating_element}\n"
        return res2