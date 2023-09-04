
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import book
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Author:
    db = "books_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Authors Models

    @classmethod
    def save(cls, data):
        query = """INSERT INTO authors (name, created_at, updated_at)
                    VALUES (%(name)s, NOW(), NOW())
                ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    # Read Authors Models

    @classmethod
    def get_all_authors(cls):
        query = """ SELECT * FROM authors
                ;"""
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for one_author in results:
            authors.append(cls(one_author))
        return authors

    @classmethod
    def get_author_with_books(cls, author_id):
        data = {
            "id": author_id
        }
        query = """SELECT * FROM authors 
                    LEFT JOIN favorites ON favorites.author_id = authors.id
                    LEFT JOIN books ON favorites.book_id = books.id 
                    WHERE authors.id = %(id)s;
                    ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        one_author = cls(results[0])
        for result in results:
            book_data = {
                'id': result['books.id'],
                'title': result['title'],
                'num_of_pages': result['num_of_pages'],
                'created_at': result['books.created_at'],
                'updated_at': result['books.updated_at'],
            }
            one_author.books.append(book.Book(book_data))
        print (one_author.books)
        return one_author

    # Update Authors Models
    


    # Delete Authors Models