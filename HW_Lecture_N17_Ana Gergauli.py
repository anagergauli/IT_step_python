from datetime import datetime

# შექმენით პითონის კლასი Car, ატრიბუტებით ბრენდით, მოდელით და წლით. ასევე, შექმენით კლასის მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.

class Car:
    total_cars_count = 0

# დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, მანქანის შექმნისას. 

    number_of_cars = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.total_cars_count += 1
        Car.number_of_cars += 1

    def car_info(self):
        print(f"ბრენდი: {self.brand}, მოდელი: {self.model}, წელი: {self.year}")

# Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს.
        
    def age_of_car(self, current_year):
        age = current_year - self.year
        print(f"მანქანის ასაკია: {age} წელი.")

# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

    @classmethod
    def total_cars(cls):
        print(f"მანქანების მთლიანი რაოდენობაა: {cls.total_cars_count}")

# შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car class-ს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
        
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life

    def battery_info(self):
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")


car1 = Car('lexus', 'ES', 2024)
car2 = Car('BMW', '3 series', 2022)
car3 = Car('Porsche', 'Cayenne', 2023)

print ("მანქანის მოდელები: ")

for car in [car1, car2, car3]:
    car.car_info()
    car.age_of_car(datetime.now().year)

electric_car1 = ElectricCar('BMW', 'ix3-e', 2022, '439')
electric_car2 = ElectricCar('Audi', 'e-tron', 2021, '222')
electric_car3 = ElectricCar('Chevrolet', 'Bolt EV', 2022, '259')

for electric_car in [electric_car1, electric_car2, electric_car3]:
    electric_car.car_info()
    electric_car.age_of_car(datetime.now().year)
    electric_car.battery_info()

Car.total_cars()