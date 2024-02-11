# 1. შექმენით ვექტორის Vector კლასი, რომელიც წარმოადგენს 2D ვექტორს. კლასს უნდა ჰქონდეს ორი ატრიბუტი x და y. კლასში დაამატეთ __add__ მეთოდი, რომ მოახდინოთ  ვექტორების დამატება და __str__ მეთოდი, რომელიც დააბრუნებს შემდეგი სახის სტრიქონს "(x, y)".
# მაგალითად:
# v1 = Vector(2, 3)
# v2 = Vector(3, 4)
# v3 = v1 + v2
# print(v3)  # Output: (5, 7)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

x1 = float(input("X კოორდინატი ვექტორი N1-ისთვის: "))
y1 = float(input("Y კოორდინატი ვექტორი N1-ისთვის: "))
x2 = float(input("X კოორდინატი ვექტორი N2-ისთვის: "))
y2 = float(input("Y კოორდინატი ვექტორი N2-ისთვის: "))

v1 = Vector(x1, y1)
v2 = Vector(x2, y2)

v3 = v1 + v2

print("ვექტორების ჯამია:", v3)


# 2. შექმენით Book კლასი, რომელსაც ექნება ორი ატრიბუტი (სათაური, ავტორი). კლასს შეუქმენით __eq__ მეთოდი რომელიც შეამოწმებს ორი წიგნის ტოლობას.
# ორი წიგნი ითვლება ტოლად თუ მათი სათაურები და ავტორები იდენტურია.

# მაგალითად:
# book1 = Book('1984', 'George Orwell')
# book2 = Book('1984', 'George Orwell')
# book3 = Book('Brave New World', 'Aldous Huxley')
# print(book1 == book2)  # Output: True
# print(book1 == book3)  # Output: False

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, book):
        return self.title == book.title and self.author == book.author

title1 = input("შეიყვანეთ პირველი წიგნის სათაური: ")
author1 = input("შეიყვანეთ პირველი წიგნის ავტორი: ")
title2 = input("შეიყვანეთ მეორე წიგნის სათაური: ")
author2 = input("შეიყვანეთ მეორე წიგნის ავტორი: ")

book1 = Book(title1, author1)
book2 = Book(title2, author2)

if(book1 == book2):
    print("თქვენ მიერ მითითებული წიგნები იდენტურია")
else:
    print("თქვენ მიერ მითითებული წიგნები განსხვავებულია")