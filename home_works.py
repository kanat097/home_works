# task 1
numbers = [i for i in range(1, 21) if i % 2 == 0]
print(numbers)

# task 2
print([i ** 2 for i in range(1, 11)])

# task 3
numbers = [5, 12, 7, 18, 3, 10, 8]
print([i for i in numbers if i > 7])

# task 4
words = ["apple", "banana", "cherry"]
print([word.upper() for word in words])

# task 5
print(["polojitelnoe" if int(input()) > 0 else "otricatelnoe"])

# task 6
print(["jup" if int(input()) % 2 == 0 else "tak"])

# rask 7
numbers = [4, -1, 7, -3, 0, 9, -2]
print([0 if i < 0 else i for i in numbers])