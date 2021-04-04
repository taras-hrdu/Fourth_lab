from .hand_tool import HandTool
from .Device import Items


class MeasuringCup(HandTool):
    def __init__(self, brand: str = "", price: int = 0, name: str = "", weight_in_kg: int = 0, color: str = "",
                 power: int = 0, guarantee: float = 0, handle_material: str = "", length_in_mm: int = 0,
                 vol: float = 0, surface_type: str = ""):
        super().__init__(Items.Involved, brand, price, name, weight_in_kg, color, power, guarantee, handle_material,
                         length_in_mm)
        self.vol = vol
        self.surface_type = surface_type

    def __str__(self):
        res5 = f"brand: {self.brand}\nprice: {self.price}\nname: {self.name}\nitems_for_cake: {self._items_for_cake}\n" \
               f"weight: {self.weight_in_kg}\ncolor: {self.color}\npower: {self.power}\nguarantee: {self.guarantee}\n" \
               f"handle_material: {self.handle_material}\nlength_in_mm: {self.length_in_mm}\n" \
               f"vol: {self.vol}\nsurface_type: {self.surface_type}\n"
        return res5