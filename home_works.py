# task #1
user_input = input("Введите слово или предложение: ")
glasnye = "аеёиоуыэюяаеёэиоуыяАЕЁИОУЫЭЮЯ"
soglasnye = "бвгдеёжзийклмнопрстфхцчшщьъБВГДЕЁЖЗИЙКЛМНОПРСТФХЦЧШЩЬЪ"
glasnye_count = 0
soglasnye_count = 0
for char in user_input:
    if char.lower() in glasnye:
        glasnye_count += 1
    elif char.lower() in soglasnye:
        soglasnye_count += 1
print(f"Гласных букв: {glasnye_count}")
print(f"Согласных букв: {soglasnye_count}")

# task #2
user_input = input("Введите числа: ")
try:
    numbers = list(map(int, user_input.split()))
    chetnye_numbers = [num for num in numbers if num % 2 == 0]
    total = sum(chetnye_numbers)
    print("Четные числа:", chetnye_numbers)
    print("Сумма четных чисел:", total)
except ValueError:
    print("Ошибка: ввод содержит нечисловые данные. Пожалуйста, введите только числа.")
