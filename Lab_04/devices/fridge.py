from .electrical_appliance import ElectricalAppliance
from .Device import Items


class Fridge(ElectricalAppliance):
    def __init__(self, brand: str = "", price: int = 0, name: str = "", weight_in_kg: int = 0, color: str = "",
                 power: int = 0, guarantee: float = 0, energy_consumption: float = 0, cord_length: float = 0,
                 number_of_buttons: int = 0, fridge_type: str = '',
                 number_of_shelves: int = 0, count_of_containers: int = 0):
        super().__init__(Items.Not_involved, brand, price, name, weight_in_kg, color, power, guarantee,
                         energy_consumption, cord_length, number_of_buttons)
        self.fridge_type = fridge_type
        self.number_of_shelves = number_of_shelves
        self.count_of_containers = count_of_containers

    def __str__(self):
        res3 = f"brand: {self.brand}\nprice: {self.price}\nname: {self.name}\nitems_for_cake: {self._items_for_cake}\n"\
        f"weight: {self.weight_in_kg}\ncolor: {self.color}\npower: {self.power}\nguarantee: {self.guarantee}\n"\
        f"energy: {self.energy_consumption}\ncord: {self.cord_length}\nnumber_of_buttons: {self.number_of_buttons}\n"\
        f"fridge_type: {self.fridge_type}\nnumber_of_shelves: {self.number_of_shelves}\ncount_of_containers: {self.count_of_containers}\n"
        return res3