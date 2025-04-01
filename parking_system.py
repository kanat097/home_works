import random
from datetime import datetime

# Тарифы (например, 100 сом в час)
TARIFF_PER_HOUR = 100

# Словарь для хранения информации о талонах
tickets = {}


def issue_ticket():
    # Ввод номера машины
    car_number = input("Введите номер машины: ")
    if not car_number.strip():
        print("Ошибка: Номер машины не может быть пустым!")
        return

    # Генерация уникального номера талона случайным образом
    ticket_number = str(random.randint(100000, 999999))
    current_time = datetime.now()

    # Сохраняем информацию о талоне
    tickets[ticket_number] = {'car_number': car_number, 'entry_time': current_time}

    # Выводим информацию о выданном талоне
    print(f"Талон выдан:")
    print(f"Номер талона: {ticket_number}")
    print(f"Номер машины: {car_number}")
    print(f"Время выдачи: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")


def calculate_parking_fee(ticket_number):
    # Проверка, существует ли талон
    if ticket_number not in tickets:
        print("Ошибка: Талон не найден!")
        return

    # Получаем данные по талону
    ticket = tickets[ticket_number]
    entry_time = ticket['entry_time']
    car_number = ticket['car_number']

    # Ввод времени выезда
    exit_time = datetime.now()

    # Расчет продолжительности парковки
    parking_duration = exit_time - entry_time
    hours_parked = parking_duration.total_seconds() / 3600  # переводим в часы

    # Расчет стоимости парковки
    fee = round(hours_parked * TARIFF_PER_HOUR)

    # Вывод счета
    print(f"\nСчет к оплате:")
    print(f"Номер талона: {ticket_number}")
    print(f"Номер машины: {car_number}")
    print(f"Время въезда: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Время выезда: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Продолжительность парковки: {int(hours_parked)} часов")
    print(f"Стоимость парковки: {fee} сом")


def main():
    while True:
        # Меню действий
        print("\nВыберите действие:")
        print("1. Выдача талона")
        print("2. Сдача талона")
        choice = input("Ваш выбор: ")

        if choice == '1':
            issue_ticket()
        elif choice == '2':
            ticket_number = input("Введите номер талона: ")
            calculate_parking_fee(ticket_number)
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()