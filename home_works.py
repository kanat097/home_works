# n = int(input())
# res = []
# for i in range(1, n + 1):
#     if i % 5 == 0:
#         res.append(i)
# print(*res)

# res = [f"{n} x {i} = {i * n}" for i in range(1, 11) if n < 10]
# print(res)

res = [i for i in range(1, int(input()) + 1) if i % 3 == 0 and i % 5 == 0]
print(res)