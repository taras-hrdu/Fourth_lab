from enum import Enum


class Items(Enum):
    Involved = 0 
    Not_involved = 1


class Device:
    def __init__(self, _items_for_cake: Items, brand: str = "", price: int = 0, name: str = "",  weight_in_kg: int = 0,
                 color: str = "", power: int = 0, guarantee: float = 0):
        self.brand = brand
        self.price = price
        self.name = name
        self._items_for_cake = Items(_items_for_cake)
        self.weight_in_kg = weight_in_kg
        self.color = color
        self.power = power
        self.guarantee = guarantee
    
    def __str__(self):
        res1 = f"brand: {self.brand} price: {self.price} name: {self.name} items_for_cake: {self._items_for_cake}"\
        f"weight: {self.weight_in_kg} color: {self.color} power: {self.power} guarantee: {self.guarantee}"
        return res1

    def get_type(self):
        return self._items_for_cake