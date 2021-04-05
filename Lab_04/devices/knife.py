from .hand_tool import HandTool
from .Device import Items


class Knife(HandTool):
    def __init__(self, brand: str = "", price: int = 0, name: str = "", weight_in_kg: int = 0,  color: str = "",
                 power: int = 0, guarantee: float = 0, handle_material: str = "", length_in_mm: int = 0,
                 handle_length: float = 0, blade_length: float = 0, number_of_blades: int = 0):
        super().__init__(Items.Involved, brand, price, name, weight_in_kg, color, power, guarantee,
                         handle_material, length_in_mm)
        self.handle_length = handle_length
        self.blade_length = blade_length
        self.number_of_blades = number_of_blades

    def __str__(self):
        res4 = f"brand: {self.brand}\nprice: {self.price}\nname: {self.name}\nitems_for_cake: {self._items_for_cake}\n"\
        f"weight: {self.weight_in_kg}\ncolor: {self.color}\npower: {self.power}\nguarantee: {self.guarantee}\n"\
        f"handle_material: {self.handle_material}\nlength_in_mm: {self.length_in_mm}\n"\
        f"handle_length: {self.handle_length}\nblade_length: {self.blade_length}\nnumber_of_blades: {self.number_of_blades}\n"
        return res4