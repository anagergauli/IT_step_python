# 1. დაწერეთ პროგრამა, რომელიც ქმნის ორ ძაფს (Thread) 30-დან 50-ის ჩათვლით ლუწი და კენტი რიცხვების მოსაძებნად. შედეგი დაბეჭდეთ ეკრანზე

import threading

def even_nums():
    even_numbers = [num for num in range(30, 51) if num % 2 == 0]
    print("Even numbers:", even_numbers)

def odd_nums():
    odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    t1 = threading.Thread(target=even_nums)
    t2 = threading.Thread(target=odd_nums)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()


# დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.

import threading
import requests


def download_mp3(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
                print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download: {filename} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to download: {filename} - Error: {e}")

if __name__ == "__main__":
    # URLs of MP3 files
    urls = [
        "https://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3",
        "https://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3",
        "https://codeskulptor-demos.commondatastorage.googleapis.com/pang/paza-moduless.mp3",
    ]

    threads = []
    for url in urls:
        filename = url.split('/')[-1]
        t = threading.Thread(target=download_mp3, args=(url, filename))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All downloads completed.")
