import model

# def user_input():
#     print("Выберите язык: ")
#     print("1. Русский (ru)")
#     print("2. Английский (en)")
#     print("3. Испанский (es)")
#     print("4. Французский (fr)")
#     print("5. Немецкий (de)")
#     print("6. Итальянский (it)")
#     choice = input("Введите код языка: ").strip()
#     print(greet(choice))
# if __name__ == "__main__":
#     user_input()
# import model
# language_code = not input("Выберите язык: ").strip().lower()
# print(model.greet(language_code))

print(model.add_user('Aida'))
print(model.get_user())
print(model.delete_user('Aida'))
print(model.get_user())