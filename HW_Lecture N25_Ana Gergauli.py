# TODO SOLID პრინციპის დაცვით შეცვალეთ კლასების იმპლემენტაცია

# Single Responsibility Principle
# class Book:
#     def set_details(self, title, author):
#         pass
#     def get_discount_price(self, discount):
#         pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def set_details(self, title, author):
        self.title = title
        self.author = author

class DiscountCalculator:
    @staticmethod
    def get_discount_price(price, discount):
        return price * (1 - discount)



# TODO დაამატეთ  PayPal-ის გადახდების კლასი, და  Payment
# Open/Closed Principle
# class Payment:
#     """  გადახდის კლასი საკრედიტო ბარათით გადახდების დასამუშავებლად
#     """
#     def process_credit(self, amount):
#         pass

from abc import ABC, abstractmethod

class Payment(ABC):
    """ Abstract base class for processing payments
    """
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    """ Class for processing credit card payments
    """
    def process_payment(self, amount):
        # Logic for processing credit card payments
        pass

class PayPalPayment(Payment):
    """ Class for processing PayPal payments
    """
    def process_payment(self, amount):
        # Logic for processing PayPal payments
        pass


# TODO გადააკეთეთ კლასები ისე, რომ დაიცვან ლისკოვის ჩანაცვლების პრინციპი
# Liskov Substitution Principle


class Vehicle:
    def fuel_capacity(self):
        return "100 liters"

class ElectricCar(Vehicle):
    def fuel_capacity(self):
        return "Battery capacity is 100 kWh"


# TODO შეცვალეთ იმპლემენტაცია, რადგან ყველა მოთამაშეს არ აქვს აუდიოს ან ვიდეოს მხარდაჭერა
# Interface Segregation Principle
# class MultimediaPlayer:
#     def play_audio(self):
#         pass
#     def play_video(self):
#         pass

class AudioPlayer:
    def play_audio(self):
        pass

class VideoPlayer:
    def play_video(self):
        pass


# TODO შეცვალეთ კლასის იმპლემენტაცია, რომ დაიცვას დამოკიდებულების ინვერსიის პრინციპი.
# Dependency Inversion Principle (DIP)
# class ConsoleDisplay:
#     def show(self, data):
#         pass

# class WeatherStation:
#     def report(self, display):
#         display.show("Weather Data")

from abc import ABC, abstractmethod

class Display(ABC):
    @abstractmethod
    def show(self, data):
        pass

class ConsoleDisplay(Display):
    def show(self, data):
        print(data)

class WeatherStation:
    def __init__(self, display):
        self.display = display

    def report(self):
        data = "Weather Data"
        self.display.show(data)

