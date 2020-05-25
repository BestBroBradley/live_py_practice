import sqlite3

# Here is a list of the SQL operations we will be doing:
# Create table:
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, genre TEXT, rating INTEGER)"

# Create new entry:
INSERT_BOOK = "INSERT INTO books (title, author, genre, rating) VALUE (?, ?, ?, ?)"

# Show all:
SHOW_ALL = "SELECT (title, author, genre, rating) FROM books"

# Show all in descending rating order:
SHOW_ALL_RATINGS = "SELECT (title, author, genre, rating) FROM books ORDER rating DESC"

# Show only the highest rated item:
SHOW_TOP = "SELECT (title, author, genre, rating) FROM books ORDER rating DESC LIMIT 1"

# Show all by author:
SEARCH_AUTHOR = "SELECT (title, author, genre, rating) FROM books WHERE author = ?"

# Show one by title:
SEARCH_TITLE = "SELECT (title, author, genre, rating) FROM books where title = ?"

# Delete from database:
DELETE_ITEM = "DELETE FROM books WHERE title = ?"


# Create db
# We will not actually be calling the function here, but in app.py instead
def open_db():
    return sqlite3.connect("data.db")


# Create books table in db with id, title, author, genre, rating (out of ten)
def create_table(connection):
    with connection:
        connection.execute(CREATE_TABLE)
        return f"Table successfully created."


# Create a function which will add a book
# Notice that this does take in input from the front end about the book
def add_book(connection, title, author, genre, rating):
    with connection:
        connection.execute(INSERT_BOOK, (title, author, genre, rating))
        return f"New book successfully added."


# Create a function which will read all books from DB
# The user is expecting data back, so this function must return data
def all_books(connection):
    with connection:
        return connection.execute(SHOW_ALL).fetchall()


# Create a function which will search by author
# Notice we are including a comma after author to tell python this is still a tuple despite having only one entry
def author_query(connection, author):
    with connection:
        return connection.execute(SEARCH_AUTHOR, (author,)).fetchall()


# Create a function which will search by title
# We are only expecting a single response from the database, so we use fetchone instead of fetchall
def title_query(connection, title):
    with connection:
        return connection.execute(SEARCH_TITLE, (title,)).fetchone()


# Create a function which will show all books in descending rating
def ratings_sort(connection):
    with connection:
        return connection.execute(SHOW_ALL_RATINGS).fetchall()


# Create a function which will show only the top rated book
def show_top(connection):
    with connection:
        return connection.execute(SHOW_TOP).fetchone()


# Create a function which will remove a book from the database
def delete_book(connection, title):
    with connection:
        connection.execute(DELETE_ITEM)
        return f"{title} Successfully deleted"


