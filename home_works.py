# task 1
name = input("Атыныз ким: ")
age = int(input("Жашыныз канчада: "))
print(f"Салам {name} !, Сен {age} жаштасын ")

# task 2
number_1 = int(input("Санды жаз: "))
number_2 = int(input("Санды жаз: "))
print(f"Сандар {number_1} + {number_2} суммасы {number_1 + number_2}")

# task 3
numbers = [3, 5, 8, 10, 15]
while True:
    x = int(input("Издоого сан: "))
    if x in numbers:
        print(f"Сан {x} табылды! ")
        break


# task 4
numbers = [7, 9, 13, 18, 21]
for num in numbers:
    if num % 2 == 0:
        print(f"Биринчи жуп сан: {num}")
        break

# task 5
while True:
    password = input("Введите пароль: ")
    if password == "1234":
        print("Доступ разрешен")
        break
    else:
        print("Неверный пароль")