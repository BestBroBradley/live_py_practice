import database


MENU_PROMPT = """Choose an option below:
1.) Show all books
2.) Search for a book
3.) Search for an author
4.) Add a book
5.) Update a book
6.) Sort books by rating
7.) Show highest rated
8.) Delete a book
9.) Exit program
    
Your selection: """


def menu():
    connection = database.open_db()
    database.create_table(connection)
    while (user_input := input(MENU_PROMPT)) != "9":
        print(user_input)
        if user_input == "1":
            show_all(connection)
        elif user_input == "2":
            search_title(connection)
        elif user_input == "3":
            search_author(connection)
        elif user_input == "4":
            add(connection)
        elif user_input == "5":
            update(connection)
        elif user_input == "6":
            sort_by_rating(connection)
        elif user_input == "7":
            show_highest(connection)
        elif user_input == "8":
            delete(connection)
        else:
            print("Invalid selection.")
    print("Goodbye.")


def show_all(connection):
    books = database.all_books(connection)
    if books:
        for book in books:
            print(book)
    else:
        print("Looks like you haven't added any books yet.")


def search_title(connection):
    query = input("What title would you like to search? ")
    result = database.title_query(connection, query)
    print(f"Search results: {result[0]} by {result[1]} (Genre: {result[2]}, Rating: {result[3]}/10)")


def search_author(connection):
    query = input("What author would you like to search? ")
    results = database.author_query(connection, query)
    if results:
        print(f"Search results for {query}:")
        for result in results:
            print(f"    -{result[0]} (Genre: {result[2]}, Rating: {result[3]}/10)")
    else:
        print(f"Looks like that author doesn't have any titles in your database.")


def add(connection):
    title = input("What book would you like to add? ")
    author = input(f"Who is the author of {title}? ")
    genre = input(f"What genre is {title}? ")
    rating = input(f"How would you rate {title} out of 10? ")
    database.add_book(connection, title, author, genre, rating)
    print(f"You added {title} by {author} to your database.")


def update(connection):
    pass


def sort_by_rating(connection):
    pass


def show_highest(connection):
    pass


def delete(connection):
    pass


menu()
