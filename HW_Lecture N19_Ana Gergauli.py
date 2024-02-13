# 1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.
# 2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.
# 3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ.

class Car:
    def __init__(self, brand, model, year):
        print("new car...")
        self._brand = None
        self._model = None
        self._year = None

        self.brand = brand
        self.model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str): 
            self._brand = value
        else:
            raise ValueError("მანქანის ბრენდი უნდა იყოს string") 

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self._model = value
        else:
            raise ValueError("მოდელი უნდა იყოს string")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, (int)):
            self._year = value
        else:
            raise ValueError("წელი უნდა იყოს მოცემული მთელი რიცხვებით")


brand = input("შეიყვანეთ მანქანის ბრენდი: ")
model = input("მიუთითეთ მანქანის მოდელი: ")
year = int(input("მიუთითეთ მანქანის გამოშვების წელი: "))

car = Car(brand=brand, model=model, year=year)
print("Brand:", car.brand)
print("Model:", car.model)
print("Year:", car.year)

new_brand = input("მიუთითეთ მანქანის ახალი ბრენდი: ")
car.brand = new_brand

new_model = input("მიუთითეთ ახალი მანქანის მოდელი: ")
car.model = new_model

new_year = int(input("მიუთითეთ ახალი მანქანის გამოშვების წელი: "))
car.year = new_year

print("განახლებული მანქანის ბრენდია:", car.brand)
print("განახლებული მანქანის მოდელია:", car.model)
print("განახლებული მანქანის გამოშვების წელია:", car.year)