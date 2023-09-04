from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author, book # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Books Controller

@app.route('/books/create', methods=["POST"])
def create_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages'],
    }
    book.Book.save(data)
    return redirect('/books')

# Read Books Controller

@app.route('/books')
def read_books():
    books = book.Book.get_all_books()
    return render_template('books.html', books = books)

@app.route('/books/<int:book_id>')
def read_book_with_authors(book_id):
    one_book = book.Book.get_book_with_authors(book_id)
    all_authors = author.Author.get_all_authors()
    return render_template('books_show.html', one_book = one_book, all_authors = all_authors)

# @app.route('/ninjas/edit/<int:ninja_id>')
# def edit_page(ninja_id):
#     one_ninja = book.Ninja.get_ninja_by_id(ninja_id)
#     print (f"in edit route with data: {one_ninja}")
#     return render_template('edit_ninja.html', one_ninja = one_ninja)

# Update Books Controller

# @app.route('/ninjas/update', methods=["POST"])
# def update_ninja():
#     book.Ninja.update(request.form)
#     return redirect(f'/dojos/{request.form["dojo_id"]}')

# Delete Books Controller

# @app.route('/ninjas/delete/<int:ninja_id>/<int:dojo_id>')
# def delete_ninja(ninja_id, dojo_id):
#     book.Ninja.delete(ninja_id)
#     return redirect(f'/dojos/{dojo_id}')


# Notes:
# 1 - Use meaningful names
# 2 - Do not overwrite function names
# 3 - No matchy, no worky
# 4 - Use consistent naming conventions 
# 5 - Keep it clean
# 6 - Test every little line before progressing
# 7 - READ ERROR MESSAGES!!!!!!
# 8 - Error messages are found in the browser and terminal




# How to use path variables:
# @app.route('/<int:id>')                                   The variable must be in the path within angle brackets
# def index(id):                                            It must also be passed into the function as an argument/parameter
#     user_info = user.User.get_user_by_id(id)              The it will be able to be used within the function for that route
#     return render_template('index.html', user_info)

# Converter -	Description
# string -	Accepts any text without a slash (the default).
# int -	Accepts integers.
# float -	Like int but for floating point values.
# path 	-Like string but accepts slashes.

# Render template is a function that takes in a template name in the form of a string, then any number of named arguments containing data to pass to that template where it will be integrated via the use of jinja
# Redirect redirects from one route to another, this should always be done following a form submission. Don't render on a form submission.