import unittest
from unittest.mock import patch
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2023)

    def test_fuel_up(self):
        with patch.object(self.vehicle, 'gaz_tank_size', 0):
            self.assertEqual(self.vehicle.fuel_up, "Gas tank is empty and can not move.")
        with patch.object(self.vehicle, 'gaz_tank_size', 45):
            self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")


class TestElectricVehicle(unittest.TestCase):

    def setUp(self):
        self.ev = ElectricVehicle("Tesla", "Model S", 2024)

    def test_fuel_up(self):
        self.assertEqual(self.ev.fuel_up, "This vehicle has no fuel tank!")

    def test_charge(self):
        self.assertEqual(self.ev.charge, "The vehicle is now charged.")

    def test_drive(self):
        self.assertEqual(self.ev.drive, "The Model S is now driving.")

if __name__ == '__main__':
    unittest.main()
