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
def create_table():
    pass


# Create a function which will add a book
def add_book(connection):
    pass


# Create a function which will read all books from DB
def all_books(connection):
    pass


# Create a function which will search by author
def author_query(connection, author):
    pass


# Create a function which will search by title
def title_query(connection, title):
    pass


# Create a function which will show all books in descending rating
def ratings_sort(connection):
    pass


# Create a function which will show only the top rated book
def show_top(connection):
    pass


# Create a function which will remove a book from the database
def delete_book(connection):
    pass


