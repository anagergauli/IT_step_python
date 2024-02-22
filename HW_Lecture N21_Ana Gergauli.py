# შექმენით ორი კლასი:
# I. Student, ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
# II. Address, ატრიბუტებით: city, street
# Student კლასის address ატრიბუტს მნიშვნელობად უნდა მიანჭოთ Address კლასის ეგზემპლარი.
# შექმენთ ორივე კლასის რამდენიმე ეგზემპლარი.
# json მოდულის დახმარებით ფაილში შეინახეთ სტუდენტები.
# მოახდინეთ წაკითხვა. შეცვალეთ ატრიბუტ(ებ)ის მნიშვნელობა (მაგ.: mark, str), დაამატეთ ახალი ატრიბუტი grade მნიშვნელობით A, B, C, D (A -> [91-100], B -> [81-90], C -> [71-80], D -> <=70).
# შეცვლილი მონაცემები შეინახეთ ფაილში.
# საბოლოო შედეგის ნიმუში (ფაილში შენახული):
# [
#   {
#     "row_id": 1,
#     "name": "Paata",
#     "mark": 87,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Saburtalo"
#     },
#     "grade": "B"
#   },
#   {
#     "row_id": 2,
#     "name": "Demetre",
#     "mark": 100,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Gldani-7-11-4-93"
#     }
#   },
#   {
#     "row_id": 3,
#     "name": "Alexander",
#     "mark": 100,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Gldani-7-11-4-93"
#     }
#   },
#   {
#     "row_id": 4,
#     "name": "Teona",
#     "mark": 92,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Gldani-7-11-4-93"
#     }
#   },
#   {
#     "row_id": 5,
#     "name": "Nino",
#     "mark": 99,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Leselidzs str. 25"
#     }
#   },
#   {
#     "row_id": 6,
#     "name": "Andria",
#     "mark": 87,
#     "address": {
#       "city": "Tbilisi",
#       "street": "Varketili IV 407-5-123"
#     }
#   }
# ]

import json

# student კლასის შექმნა ატრიბუტებით: name, mark, address, სტატიკური ატრიბუტი row_id
class Student:
    row_id = 1

    def __init__(self, name, mark, address, grade=None):
        self.row_id = Student.row_id
        Student.row_id += 1
        self.name = name
        self.mark = mark
        self.address = address
        self.grade = grade if grade else self.calc_grade()

    def calc_grade(self):
        if self.mark >= 91:
            return 'A'
        elif self.mark >= 81:
            return 'B'
        elif self.mark >= 71:
            return 'C'
        else:
            return 'D'
# Address კლასის შექმნა ატრიბუტებით: city, street
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

class Enc(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "row_id": obj.row_id,
                "name": obj.name,
                "mark": str(obj.mark), 
                "address": obj.address.__dict__,
                "grade": obj.grade
            }
        elif isinstance(obj, Address):
            return {
                "city": obj.city,
                "street": obj.street
            }
        return super().default(obj)

# Address კლასის ეგზემპლარები
address1 = Address("Tbilisi", "Saburtalo")
address2 = Address("Tbilisi", "Gldani-7-11-4-93")
address3 = Address("Tbilisi", "Leselidzs str. 25")
address4 = Address("Tbilisi", "Varketili IV 407-5-123")

# Student კლასის ეგზემპლარები
student1 = Student("Paata", 87, address1)
student2 = Student("Demetre", 100, address2)
student3 = Student("Alexander", 100, address2)
student4 = Student("Teona", 92, address2)
student5 = Student("Nino", 99, address3)
student6 = Student("Andria", 87, address4)

students = [student1, student2, student3, student4, student5, student6]

# მონაცემების შენახვა JSON ფაილში
with open('students.json', 'w') as f:
    json.dump(students, f, cls=Enc, indent=4)

print("Data saved to 'students.json'")
