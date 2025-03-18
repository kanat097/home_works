# task 1
def season(month):
#     if 1 <= month <= 2 or month == 12:
#         return "Winter"
#     elif 3 <= month <= 5:
#         return "Spring"
#     elif 6 <= month <= 8:
#         return "Summer"
#     elif 9 <= month <= 11:
#         return "Autumn"
#     else:
#         return "Fall"




 if month in [1,2, 12]:
    return "Winter"
 elif month in [3, 4, 5,]:
    return "Spring"
 elif month in [6, 7, 8]:
    return "Summer"
 elif month in [9, 10, 11]:
    return "Autumn"
 else:
    return "Fall"



def is_date(day, month, year):
    from datetime import date
    return date(year, month, day)
print(is_date(18, 3, 2025))
print(is_date(29, 2, 2025))

def func(a, b, c):
    pass
func(1, 2, 3)