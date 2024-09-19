import random

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    
    print("Угадай число от 1 до 100")
    
    while True:
        guess = int(input("Введи свое предположение: "))
        
        if guess < number:
            print("Загаданное число больше")
        elif guess > number:
            print("Загаданное число меньше")
        else:
            print(f"Поздравляю! Ты угадал число за {tries} попыток!")
            break
        
        tries += 1

guess_number()
