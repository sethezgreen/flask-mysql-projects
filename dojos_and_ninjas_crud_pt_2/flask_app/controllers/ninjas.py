from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo, ninja # import entire file, rather than class, to avoid circular imports
# As you add model files add them the the import above
# This file is the second stop in Flask's thought process, here it looks for a route that matches the request

# Create Ninjas Controller

@app.route('/ninjas/create', methods=["POST"])
def create_ninja():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id']
    }
    ninja.Ninja.save(data)
    return redirect('/dojos')

# Read Ninjas Controller

@app.route('/ninjas')
def new_ninja_form():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos = dojos)

@app.route('/ninjas/edit/<int:ninja_id>')
def edit_page(ninja_id):
    one_ninja = ninja.Ninja.get_ninja_by_id(ninja_id)
    print (f"in edit route with data: {one_ninja}")
    return render_template('edit_ninja.html', one_ninja = one_ninja)

# Update Ninjas Controller

@app.route('/ninjas/update', methods=["POST"])
def update_ninja():
    ninja.Ninja.update(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')

# Delete Ninjas Controller

@app.route('/ninjas/delete/<int:ninja_id>/<int:dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    ninja.Ninja.delete(ninja_id)
    return redirect(f'/dojos/{dojo_id}')


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