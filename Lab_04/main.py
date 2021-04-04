from devices import DeviceManager
from devices import Items,  Kettle, Fridge, Knife, MeasuringCup


class DeviceTest:
    def __init__(self):
        pass

    def main(self):
        device = DeviceManager()
        device.add_devices([
            Kettle("Phillips",  25, "BronzeHero", 20, "black", 20, 2.4, 1.3, 3.2, 5, 12, "Hit"),
            Fridge("Panasonic", 19, "MyFridge", 17, "green", 15, 1.2, 1.3, 3.2, 5, "Hit", 4, 7),
            Knife("Buck", 80, "HandMadeKnife", 1, "red", 10, 10.5, "Gold", 100, 9.2, 3.2, 5),
            MeasuringCup("Kenon", 2, "Cup4Family", 200, "white", 5, 1.2,"Leather", 203, 60, "Plastic")
        ])

        print('     Sorted by price\n\n' + '\n'.join([str(x) for x in device.sort_by_price(True)]), '\n')
        print('     Sorted by power:\n\n' + '\n'.join([str(x) for x in device.sort_by_power()]), '\n')
        print('     Find for cooking cake:\n\n' + '\n'.join([str(x) for x in device.sort_by_power(False,
                                                device.find_by_items(Items.Involved))]), '\n')


if __name__ == '__main__':
    test = DeviceTest()
    test.main()
