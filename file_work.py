# # Записать в файл
# with open('file.txt', 'r') as file:
#     content = file.write('Hello, World!')
#
# # Дописать в файл
# with open('file1.txt', 'r') as file:
#     file.write('\nThis is a new line.')
#     print(content)
#
# # Прочитать файл
# with open('file.txt', 'r') as file:
#     content = file.read()
#     print(content)
#
# # Создать файл
# with open('file.txt', 'x') as file:
#     file.write('This is a new file')

# # Запись и чтение файла
# with open('file.txt', 'w+') as file:
#     file.write('Hello, Kanat!\nThis is a new line.')
#     file.seek(0) # Переместить курсор в начало файла
#     content = file.read()
#     print(content)


with open('numbers.txt', 'w') as file:
    for i in range(5):
      number = int(input("Vvedite chislo: "))
      file.write(f'{number}\n')

numbers = []
with open('numbers.txt', 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))
    print(sum(numbers))