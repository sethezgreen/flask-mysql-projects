from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import author, book # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

@app.route('/')
def index():
    return redirect('/authors')

# Create Authors Controller

@app.route('/authors/create', methods=["POST"])
def create_author():
    author.Author.save(request.form)
    return redirect('/')

# Read Authors Controller

@app.route('/authors')
def read_authors():
    authors = author.Author.get_all_authors()
    return render_template('authors.html', authors = authors)

@app.route('/authors/<int:author_id>')
def read_author_with_books(author_id):
    one_author = author.Author.get_author_with_books(author_id)
    all_books = book.Book.get_all_books()
    return render_template('authors_show.html', one_author = one_author, all_books = all_books)


# Update Authors Controller



# Delete Authors Controller


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