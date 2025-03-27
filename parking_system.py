# import time
#
# TARIFF = 100  # 100 сом за час
# tickets = {}  # Хранение активных талонов
#
#
# def issue_ticket():
#     car_number = input("Введите номер машины: ").strip()
#     if not car_number:
#         print("Ошибка: номер машины не может быть пустым.")
#         return
#
#     ticket_id = str(len(tickets) + 1)  # Упрощённый ID талона
#     tickets[ticket_id] = time.time()  # Запоминаем время въезда
#
#     print(f"Талон №{ticket_id} выдан!")
#
#
# def return_ticket():
#     ticket_id = input("Введите номер талона: ").strip()
#
#     if ticket_id not in tickets:
#         print("Ошибка: талон не найден.")
#         return
#
#     entry_time = tickets.pop(ticket_id)
#     hours = max(1, int((time.time() - entry_time) // 3600))  # Минимум 1 час
#     print(f"К оплате: {hours * TARIFF} сом.")
#
#
# def main():
#     while True:
#         choice = input("\n1 - Выдать талон\n2 - Сдать талон\n3 - Выход\nВыбор: ")
#         if choice == "1":
#             issue_ticket()
#         elif choice == "2":
#             return_ticket()
#         elif choice == "3":
#             break
#         else:
#             print("Ошибка: неверный выбор.")
#
#
# if __name__ == "__main__":
#     main()

import time

# Тариф за час
TARIFF_PER_HOUR = 100

# Хранилище талонов (просто словарь)
parking_data = {}

# Генерация номера талона (просто текущее время в секундах)
def generate_ticket_number():
    return str(int(time.time()))

# Выдача талона
def issue_ticket():
    car_number = input("Введите номер машины: ").strip().upper()

    # Проверяем, что номер машины не пустой
    if not car_number:
        print("Ошибка: Введите правильный номер машины.")
        return

    ticket_number = generate_ticket_number()
    entry_time = time.time()  # Запоминаем время въезда в секундах

    # Сохраняем данные
    parking_data[ticket_number] = {"car_number": car_number, "entry_time": entry_time, "paid": False}

    print("\nТалон выдан:")
    print("Номер талона:", ticket_number)
    print("Номер машины:", car_number)
    print()

# Сдача талона и расчет стоимости
def return_ticket():
    ticket_number = input("Введите номер талона: ").strip()

    if ticket_number not in parking_data:
        print("Ошибка: Талон не найден.")
        return

    if parking_data[ticket_number]["paid"]:
        print("Ошибка: Талон уже оплачен.")
        return

    entry_time = parking_data[ticket_number]["entry_time"]
    exit_time = time.time()  # Текущее время
    duration_hours = int((exit_time - entry_time) // 3600) + 1  # Округляем вверх
    total_cost = duration_hours * TARIFF_PER_HOUR

    print("\nСчет к оплате:")
    print("Номер талона:", ticket_number)
    print("Номер машины:", parking_data[ticket_number]["car_number"])
    print("Продолжительность парковки:", duration_hours, "час(ов)")
    print("Стоимость парковки:", total_cost, "сом")
    print()

    # Отмечаем талон как оплаченный
    parking_data[ticket_number]["paid"] = True

# Главное меню
def main():
    while True:
        print("\nВыберите действие:")
        print("1. Выдача талона")
        print("2. Сдача талона")
        print("3. Выход")

        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            issue_ticket()
        elif choice == "2":
            return_ticket()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный ввод, попробуйте снова.")

# Запуск программы
main()