from random import choice


def computer_choice():
    return choice(["Камень", "Ножницы", "Бумага"])


def user_choice():
    print("1: Камень")
    print("2: Ножницы")
    print("3: Бумага")
    choice_ = int(input("Выберите один из них:"))
    if choice_ == 2:
        return "Камень"
    elif choice_ == 3:
        return "Бумага"
    else:
        return -1


def check(c_choice, u_choice):
    if c_choice == user_choice:
        return "Ничья"
    elif c_choice == "Камень" and u_choice == "Ножницы":
        print(f"Computer: {c_choice} - User: {u_choice}")
        return "Вы проиграли"
    elif c_choice == "Ножницы" and u_choice == "Бумага":
        print(f"Computer: {c_choice} - User: {u_choice}")
        return "Вы проиграли"
    elif c_choice == "Бумага" and u_choice == "Камень":
        print(f"Computer: {c_choice} - User: {u_choice}")
        return "Вы проиграли"
    else:
        print(f"Computer: {c_choice} - User: {u_choice}")
        return "Ураа! Вы выиграли"

def main():
    while True:
        print("1. Начать")
        print("2. Выйти из игры")
        choice_ = int(input("Выбери: "))
        if choice_ == 1:
            while True:
                com_ch = computer_choice()
                us_ch = user_choice()
                if us_ch == -1:
                    print("Неправильный выбор")
                    continue
                res = check(com_ch, us_ch)
                print(res)
        elif choice_ == 2:
            break
        else:
            print("tuura emes")
main()
