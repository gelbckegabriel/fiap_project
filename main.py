from functions.functions import *

say_my_name('Gabriel')
users = {}
new_users = {}
counter_registered_users = 0
content = open("db.txt", "r")


def create_dictionary(archive):
    keys = []
    values = []

    for line in archive.readlines():
        key = line.split(":")
        keys.append(key[0])
        value = line.split("'")
        values.append(value[1])
        values.append(value[3])

    for key in keys:
        users[key] = [values[0], values[1]]
        values.pop(1)
        values.pop(0)


def search_user(login):
    user_found = False
    for user in users:
        if login == user:
            user_found = True
            print(f"USER '{user}' \n" +
                  f"Name.......: {users[login][0]}\n" +
                  f"Password...: {users[login][1]}\n"
                  )
    if not user_found:
        print('User not found!\n')


def delete_user(login):
    user_found = False
    for user in users:
        if login == user:
            user_found = True
    if user_found:
        del users[login]
        print(f"User '{login}' deleted with success!\n")
    else:
        print('User not found!\n')

    with open('db.txt', 'w') as archive:
        for login, value in users.items():
            archive.write(login + ": " + str(value) + "\n")
        new_users.clear()


def list_all_users():
    print('\n--------------------------------\n')
    for user in users:
        print(f"USER '{user}' \n" +
            f"Name.......: {users[user][0]}\n" +
            f"Password...: {users[user][1]}\n"
        )
    # for line in content.readlines():
    #     print(line, end="")
    # print()
    print('--------------------------------\n')


def save():
    with open('db.txt', "a") as archive:
        for login, value in new_users.items():
            archive.write(login + ": " + str(value) + "\n")


create_dictionary(content)
option = options_question()
while option == 'I' or option == 'S' or option == 'D' or option == 'L':
    if option == 'I':
        name = input('\nType the name of the user: ').upper()
        password = input('Type the password of the user: ')
        key = input('Type the login: ').upper()
        users[key] = [name, password]
        new_users[key] = [name, password]
        print('')
    elif option == 'S':
        user_login = input('\nType the login of the desired user: ').upper()
        search_user(user_login)
    elif option == 'D':
        user_login = input('\nType the login of the desired user: ').upper()
        delete_user(user_login)
    elif option == 'L':
        list_all_users()
    option = options_question()

save()
