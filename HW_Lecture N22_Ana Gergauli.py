#           დავალება N1. 
# შექმენი ფუნქცია, რომელიც მიიღებს არგუმენტად ობიექტს, ეცდება მის სრიალიზაციას json-ის დახმარებით და ფაილში შეინახავს ინფორმაციას.
# თუ ვერ შეინახა, დაბეჭდავს შესაბამის ტექსტს, შემდეგ კი ეცდება pickle-ს გამოყენებას და დაშიფრულ ობიექტს შეინახავს ფაილში.
# ესეც თუ ვერ შეძლო, დაბეჭდავს: ობიექტის სერიალიზაცია ვერ მოხერხდა.

import json
import pickle

def save_obj(obj, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(obj, file)
        print("Object is saved.")
    except Exception as e_json:
        print(f"JSON serialization failed: {e_json}")
        try:
            with open(filename, 'wb') as file:
                pickle.dump(obj, file)
            print("Object saved using pickle serialization.")
        except Exception as e_pickle:
            print(f"Pickle serialization failed: {e_pickle}")
            print("Object serialization failed.")

obj = {'a': 10, 'b': 20, 'c': 25}
save_obj(obj, 'data.json')


#                   დავალება 2
# შექმენი ფუნქცია, რომელიც არგუმენტად მოითხოვს დაშიფრული ფაილის სახელს და json-ის დახმარებით შეეცდება მიწოდებული მონაცემის დესერიალიზაციას, აღდგენილ ინფორმაციის დაბეჭდავს.
# წარუმატებლობის შემთხვევაში იგივეს შეეცდება pickle-ს საშუალებით.

def load_object(file_name):
    try:
        with open(file_name, 'r') as file:
            obj = json.load(file)
        print("Object loaded from file using JSON deserialization:")
        print(obj)
    except Exception as e_json:
        print(f"JSON deserialization failed: {e_json}")
        try:
            with open(file_name, 'rb') as file:
                obj = pickle.load(file)
            print("Object loaded from file using pickle deserialization:")
            print(obj)
        except Exception as e_pickle:
            print(f"Pickle deserialization failed: {e_pickle}")

load_object('data.json') 

#             დავალება N3
# წინა ორი პუნქტი გაიმეორე dill-ის გამოყენებით. dill-სთვის ცვლადში შეინახე მარტივი ლამბდა ფუნქცია.

# შუალედურ პროექტებს ვაკეთებ და ამ დავალებას მოგვიანებით დავასრულებ თუ შეიძლება
