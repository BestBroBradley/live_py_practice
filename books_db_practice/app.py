import database


MENU_PROMPT = """Choose an option below:
1.) Show all books
2.) Search for a book
3.) Search for an author
4.) Add a book
5.) Sort books by rating
6.) Show highest rated
7.) Delete a book
8.) Exit program
    
Your selection: """


def menu():
    connection = database.open_db()
    database.create_table(connection)
    while user_input := input(MENU_PROMPT) != "8":
        # 1.) Show all books
        if user_input == "1":
            pass
        # 2.) Search for a book
        elif user_input == "2":
            pass
        # 3.) Search for an author
        elif user_input == "3":
            pass
        # 4.) Add a book
        elif user_input == "4":
            pass
        # 5.) Sort books by rating
        elif user_input == "5":
            pass
        # 6.) Show highest rated
        elif user_input == "6":
            pass
        # 7.) Delete a book
        elif user_input == "7":
            pass
        else:
            print("Invalid selection.")
    print("Goodbye.")

menu()