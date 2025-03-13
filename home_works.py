# function - функция
def func():
    print("python")
    print("java")
    print("c++")
    print("#" * 10)
# pr = print
# pr("my name is arsen")

def area_circle():
    radius = float(input("Enter the radius: "))
    s = 3.14 * radius ** 2
    print("Аянт = ", s)
area_circle()


def area_rectangle(width, height):
    if width < 0 or height < 0:
        print("Торт бурчутуктун жактары терс сан болбойт ")
    else:
        area = width * height
        print("Аянт = ", area)
area_circle()
area_rectangle(10, 11)


def i(name):
   print(f"your's name {name} ")
name = input("Enter your name: ")
i(name)
