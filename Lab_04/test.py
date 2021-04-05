import unittest

from devices.Device import Items
from devices.device_manager import DeviceManager
from devices.measuring_cup import MeasuringCup
from devices.knife import Knife
from devices.fridge import Fridge
from devices.kettle import Kettle


class DeviceManagerTest(unittest.TestCase):

    def setUp(self):
        self.fridge = Fridge()
        self.kettle = Kettle()
        self.knife = Knife()
        self.measuring_cup = MeasuringCup()
        self.manager = DeviceManager()
        self.manager.add_device(self.fridge)
        self.manager.add_device(self.kettle)
        self.manager.add_device(self.knife)
        self.manager.add_device(self.measuring_cup)

    def test_find_by_items_Involved(self):
        expected_devices = [self.knife, self.measuring_cup]

        result = self.manager.find_by_items(Items.Involved)
        self.assertNotIn(self.kettle, result)
        self.assertNotIn(self.fridge, result)
        self.assertEqual(result, expected_devices)

    def test_find_by_items_Not_involved(self):
        expected_devices = [self.fridge, self.kettle]

        result = self.manager.find_by_items(Items.Not_involved)
        self.assertIn(self.fridge, result)
        self.assertIn(self.kettle, result)
        self.assertEqual(result, expected_devices)

    def test_sort_by_price(self):
        expected_device = [self.fridge, self.kettle, self.knife, self.measuring_cup]

        result = self.manager.sort_by_price(devices=expected_device)

        self.assertEqual(result, expected_device)

    def test_sort_by_power(self):
        expected_device = [self.fridge, self.kettle, self.knife, self.measuring_cup]

        result = self.manager.sort_by_power(devices=expected_device)

        self.assertEqual(result, expected_device)


class DeviceTest(unittest.TestCase):

    def setUp(self):
        self.fridge = Fridge()
        self.kettle = Kettle()
        self.knife = Knife()
        self.measuring_cup = MeasuringCup()

    def test_fridge(self):
        expected_device = Fridge("Panasonic", 19, "MyFridge", 17, "green", 15, 1.2, 1.3, 3.2, 5, "Hit", 4, 7)

        self.assertEqual(expected_device.brand, "Panasonic")
        self.assertEqual(expected_device.price, 19)
        self.assertEqual(expected_device.name, "MyFridge")
        self.assertEqual(expected_device.weight_in_kg, 17)
        self.assertEqual(expected_device.color, "green")
        self.assertEqual(expected_device.power, 15)
        self.assertEqual(expected_device.guarantee, 1.2)
        self.assertEqual(expected_device.energy_consumption, 1.3)
        self.assertEqual(expected_device.cord_length, 3.2)
        self.assertEqual(expected_device.number_of_buttons, 5)
        self.assertEqual(expected_device.fridge_type, "Hit")
        self.assertEqual(expected_device.number_of_shelves, 4)
        self.assertEqual(expected_device.count_of_containers, 7)

    def test_kettle(self):
        expected_device = Kettle("Phillips",  25, "BronzeHero", 20, "black", 20, 2.4, 1.3, 3.2, 5, 12, "Hit")

        self.assertEqual(expected_device.brand, "Phillips")
        self.assertEqual(expected_device.price, 25)
        self.assertEqual(expected_device.name, "BronzeHero")
        self.assertEqual(expected_device.weight_in_kg, 20)
        self.assertEqual(expected_device.color, "black")
        self.assertEqual(expected_device.power, 20)
        self.assertEqual(expected_device.guarantee, 2.4)
        self.assertEqual(expected_device.energy_consumption, 1.3)
        self.assertEqual(expected_device.cord_length, 3.2)
        self.assertEqual(expected_device.number_of_buttons, 5)
        self.assertEqual(expected_device.volume, 12)
        self.assertEqual(expected_device.heating_element, "Hit")

    def test_knife(self):
        expected_device = Knife("Buck", 80, "HandMadeKnife", 1, "red", 10, 10.5, "Gold", 100, 9.2, 3.2, 5)

        self.assertEqual(expected_device.brand, "Buck")
        self.assertEqual(expected_device.price, 80)
        self.assertEqual(expected_device.name, "HandMadeKnife")
        self.assertEqual(expected_device.weight_in_kg, 1)
        self.assertEqual(expected_device.color, "red")
        self.assertEqual(expected_device.power, 10)
        self.assertEqual(expected_device.guarantee, 10.5)
        self.assertEqual(expected_device.handle_material, "Gold")
        self.assertEqual(expected_device.length_in_mm, 100)
        self.assertEqual(expected_device.handle_length, 9.2)
        self.assertEqual(expected_device.blade_length, 3.2)
        self.assertEqual(expected_device.number_of_blades, 5)
    
    def test_measuring_cup(self):
        expected_device = MeasuringCup("Kenon", 2, "Cup4Family", 200, "white", 5, 1.2, "Leather", 203, 60, "Plastic")

        self.assertEqual(expected_device.brand, "Kenon")
        self.assertEqual(expected_device.price, 2)
        self.assertEqual(expected_device.name, "Cup4Family")
        self.assertEqual(expected_device.weight_in_kg, 200)
        self.assertEqual(expected_device.color, "white")
        self.assertEqual(expected_device.power, 5)
        self.assertEqual(expected_device.guarantee, 1.2)
        self.assertEqual(expected_device.handle_material, "Leather")
        self.assertEqual(expected_device.length_in_mm, 203)
        self.assertEqual(expected_device.vol, 60)
        self.assertEqual(expected_device.surface_type, "Plastic")


if __name__ == '__main__':
    unittest.main()
