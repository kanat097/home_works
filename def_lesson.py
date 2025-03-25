# def main(name, age):
#     return f'Привет, меня зовут {name}, мне {age}'
# print(main(age=12, name='Канат'))


'''
main(name='Kanat') - именованный
main('Kanat') - позиционный
def main(name='Kanat') - дефолтное значение, не обязательный аргумент
'''
from keyword import kwlist

from pkg_resources.extern import names


#
# def custom_sum(*args):
#     return sum(args)
# print(custom_sum(2, 4, 5, 6, 7, 7, 2, 4, 5))

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# print_info(name="Anna", age=25, city="Moscow")
# print_info(width=20, height=20)



# def create_profile(*hobbies, **info):
#     print(f'Hobbi: {hobbies}')
#     for key, value in info.items():
#         print(f"{key}: {value}")
# create_profile('чтение', 'tennis',  name="Ivan", age=30, city='bishkek')


# homework 22.03.25
with open('data.txt', 'r') as file:
    lines = file.readlines()

with open('filtered_data.txt', 'w') as filtered_data:
    for line in lines:
        if line.strip():
            filtered_data.write(line)