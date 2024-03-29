import Pytest
from vehicle import Vehicle, ElectricVehicle

def test_vehicle_fuel_up():
    car = Vehicle("Toyota", "Camry", 2022)
    assert car.fuel_up == "Gas tank is now full or can move."

def test_vehicle_drive():
    car = Vehicle("Toyota", "Camry", 2022)
    assert car.drive == "The Camry is now driving."

def test_electric_vehicle_charge():
    electric_car = ElectricVehicle("Tesla", "Model S", 2023)
    assert electric_car.charge == "The vehicle is now charged."

def test_electric_vehicle_fuel_up():
    electric_car = ElectricVehicle("Tesla", "Model S", 2023)
    assert electric_car.fuel_up == "This vehicle has no fuel tank!"

if __name__ == "__main__":
    Pytest.main()
