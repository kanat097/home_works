# бул чексиз цикл
summ = 0
while True:
    number = int(input("Enter the number: "))
    if number == 0:
        # break бул циклди токтотот
        break
    summ += number
    print(f"Общая сумма = {summ}")
