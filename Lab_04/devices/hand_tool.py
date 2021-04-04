from .Device import Device, Items


class HandTool(Device):
    def __init__(self, items_for_cake: Items, brand: str = "", price: int = 0, name: str = "", weight_in_kg: int = 0,
                 color: str = "", power: int = 0, guarantee: float = 0,
                 handle_material: str = "", length_in_mm: int = 0):
        super().__init__(Items.Involved, brand, price, name,  weight_in_kg, color, power, guarantee)
        self.handle_material = handle_material
        self.length_in_mm = length_in_mm