# '''
# [выражение for элемент in список if условие]
#
# [выражение - что делать с каждым элементом]
#
# for элемент in список - перебор элементов по отдельности]
#
# if условие - (необязательно) условие, фильтр для элементов]
# '''
#
# numbers = [x for x in range(5)]
# print(numbers)
# # for i in numbers:
# #     print(i)
# numbers = []
# for x in range(5):
#     numbers.append(x)
#
#
# # even_numbers = [x for x in range(10) if x % 2 == 0]
# # print(even_numbers)
# words = ['apple', 'orange', 'cherry']
# short_words = [word.upper() for word in words]
# print(short_words)
from operator import length_hint

# numbers = tuple(x for x in range(100))
# print(numbers)
#
# numbers = [x for x in range(10) if x % 2 != 0]
# print(numbers)
#
#
# def word_lengths(words):
#     for word in words:
#         yield len(word)
# words = ['cat', 'elephant', 'dog', 'giraffe']
# lengths = list(word_lengths(words))
# print(lengths)
#
# words = ['cat', 'elephant', 'dog', 'giraffe', 'lion']
# even_words = [word for word in words if len(word) % 2 == 0]
# print(even_words)


# homework
words = ['apple', 'banana', 'avocado', 'cherry', 'apricot',]
filtered_words = [word for word in words if word.startswith('a')]
print(filtered_words)