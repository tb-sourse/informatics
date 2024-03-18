amount_stone = int(input("Количество камней: "))

max_temperature = 100

current_temperature = 0

count = 0

import time
import random


def check_temp():
    global max_temperature, current_temperature

    if current_temperature >= max_temperature:
        print("Перегрев")
        return True
    else:
        return False


def get_stone():
    global amount_stone, current_temperature, count

    print('Камень')
    amount_stone -= 1
    count += 1
    current_temperature += random.randint(1, 20)

def chill():
    global current_temperature
    # time.sleep(1)
    current_temperature -= random.randint(1,20)


while amount_stone > 0:
    print("Камень")
    amount_stone -= 1
    count += 1
    current_temperature += random.randint(1, 20)
    if current_temperature >= max_temperature:
        print("Перегрев")
        break
    else:
        current_temperature -= random.randint(1, 20)
        continue

print("Перенесенные камни:",count)

# factorial = 1
# for i in range(6):
#     factorial *= i+1

# print(factorial)
