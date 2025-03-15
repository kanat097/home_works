from home_works import computer_choice, user_choice, check

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
