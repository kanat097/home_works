# # '''
# # lambda аргумент: выражение
# # '''
# #
# # square = lambda a, b: a + b
# # print(square(1, 4))
# # string_func = lambda a: a
# # print(string_func('Hello, World!'))
# #
# # greeting = lambda: 'Hello'
# # print(greeting())
#
# # map() - применение функции ко всем элементам списка
# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)
#
# # filtered() - фильтрация элементов списка
# numbers = [10, 15, 20, 25, 30]
# filtered = list(filter(lambda x: x % 2 == 0, numbers))
# print(filtered)
#
# length = lambda a : len(a)
# print(length('Python'))
#
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x * 3, numbers))
# print(result)
#
# words = ['cat', 'car', 'beard', 'elephant', 'computer']
# filtered_words = list(filter(lambda x: len(x) > 5, words))
# print(filtered_words)

# sorted() - сортировка с кастомным ключом
words = ['apple', 'ananas', 'banana', 'pear']
sorted_words = sorted(words, key=lambda x: len (x))
print(sorted_words)