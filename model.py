# def custom_sum(a, b):
#     return a + b
# def custom_sub(a, b):
#     return a - b

# Lang = {
#     'ru': 'Привет',
#     'en': 'Hello',
#     'es': 'Hola',
#     'fr': 'Bojour',
#     'de': 'Hallo',
#     'it': 'Ciao',
# }
#
# def greet(a):
#     if a in Lang:
#         return Lang[a]
#     else:
#         return "Language not supported"

user_data = []
def add_user(username):
    return f'Пользователь {username} добавлен'
def get_user():
    return user_data
def delete_user(username):
    if username in user_data:
        user_data.remove(username)
        return f'Пользователь {username} удален'
    else:
        return f'Пользователь {username} не найден'
