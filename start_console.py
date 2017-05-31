import psycopg2
from sql_query import *


def start_module():
    while True:
        handle_menu()
        try:
            if choose() == "exit":
                break
        except KeyError as err:
            print('choose a number')


def choose():
    option = input("Please enter a number: ")
    if option == "1":
        table = database_connection(select_name)
        print('\n         Name of Mentors   ')
        print_table(table, ['First_name', 'Last_name'])
    elif option == "2":
        table = database_connection(miskolc_nick_name)
        print_table(table, ['Nicknames'])
    elif option == "3":
        database_connection(find_carol)
    elif option == "4":
        database_connection(find_hat_girl)
    elif option == "5":
        database_connection(new_applicant_data)
    elif option == "6":
        database_connection(change_phone_number)
    elif option == "7":
        database_connection(delete_applicant)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["Names of all Mentors",
               "Nickname of Mentors in Miskolc",
               "Find Carol's full name and phone number",
               "Find the applicant who went to the Adipiscingenimmi University",
               "Add new applicant (Markus Schaffarzyk)",
               "Update Jemima Foreman phone number",
               "Delete two applicants who applied with emails for mauriseu.net dodatabase_connection"]

    print("\n", 'Basic SQL', "\n")
    for index, option in enumerate(options):
        print(" ({0}) {1}".format(index + 1, option))
    print(" (0)", 'Exit')


def print_table(table, title_list):
    max_lenght = []
    for i in range(len(title_list)):
        max_table = max([len(ta_row[i]) for ta_row in table])
        if max_table > len(title_list[i]):
            max_lenght.append(max_table + 2)
        else:
            max_lenght.append(len(title_list[i]) + 2)
    print("/", end="")
    for le in max_lenght:
        print("-" * le, end="-")
    print("-\\\n|", end="")
    for lng, title in zip(max_lenght, title_list):
        print("{0:^{width}}".format(title, width=lng), "|", end="")
    print("")
    for row in table:
        print("|", end="")
        for lng in max_lenght:
            print("-" * lng, end="-|")
        print("\n|", end="")
        for lng, field in zip(max_lenght, row):
            print("{0:^{width}}".format(field, width=lng), "|", end="")
        print("")
    print("\\", end="")
    for le in max_lenght:
        print("-" * le, end="--")
    print("\b/")


if __name__ == '__main__':
    start_module()
