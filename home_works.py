# try-except
# try:
#     a = int(input())
#     b = int(input())
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Sandy nolgo bolgongo bolboit!")
# except ValueError:
#     print("Textti sanga aylandrganga bolboit!")
# except Exception:
#     print("Kandaydyr bir kata bar")

def is_date(day, month, year):
    from datetime import date
    try:
        return date(year, month, day)
    except ValueError:
        return "Kalendarda mynday data jok"
print(is_date(18, 3, 2025))
print(is_date(29, 2, 2025))


numbers = [1,2,3,4,5]
def get_element():
    try:
        index = int(input("Vvedite index elementa: "))
        return numbers[index]
    except IndexError:
       return "Mynday index menen element jok!"
    except Exception:
       return "Kandaidyr bir kata bar"

