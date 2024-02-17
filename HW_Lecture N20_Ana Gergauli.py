# 1. შექმენით პითონის კლასი Node რომელსაც ექნება ორი ატრიბუტი (value, next), შემდეგ შექმენით LinkedList  კლასი რომლის კონსტრუქტორი მიიღებს Value პარამეტრს.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head

# 2. LinkedList კლასში შექმენით append მეთოდი, რომლის საშუალებითაც ჩაამტებთ სიის ბოლოში ახალ ნოუდს (Node  კლასის ახალ ობიექტს)
        
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

# 3. LinkedList კლასში შექმენით remove მეთოდი, რომლის საშუალებითაც წაშლით სიიდან მის ბოლო ელემენტს(Тail-ს)
        
    def remove(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        current = self.head
        while current.next != self.tail:
            current = current.next
        current.next = None
        self.tail = current

# 4. პითონის Stack.py ფაილში შექმენილია Stack კლასი, დაწერეთ კლასის ფუნქციები (push და pop)

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

