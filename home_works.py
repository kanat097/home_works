# a = 20
# if a % 2 == 0:
#     print("jup")
# else:
#     print("tak")

# print("jup" if int(input()) % 2 == 0 else "tak")

print(
    ["jup" if i % 2 == 0 else "tak"
     for i in range(int(input()) + 1)]
)