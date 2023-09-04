
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import author
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Book:
    db = "books_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Books Models

    @classmethod
    def save(cls, data):
        query = """ INSERT INTO books (title, num_of_pages, created_at, updated_at)
                    VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW())
                ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    # Read Books Models

    @classmethod
    def get_all_books(cls):
        query = """SELECT * FROM books
                ;"""
        return connectToMySQL(cls.db).query_db(query)
    
    @classmethod
    def get_book_with_authors(cls, book_id):
        data = {
            "id": book_id
        }
        query = """SELECT * FROM books 
                    LEFT JOIN favorites ON favorites.book_id = books.id
                    LEFT JOIN authors ON favorites.author_id = authors.id 
                    WHERE books.id = %(id)s;
                    ;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        one_book = cls(results[0])
        for result in results:
            author_data = {
                'id': result['authors.id'],
                'name': result['name'],
                'created_at': result['authors.created_at'],
                'updated_at': result['authors.updated_at'],
            }
            one_book.authors.append(author.Author(author_data))
        return one_book

    # @classmethod
    # def get_ninja_by_id(cls, ninja_id):
    #     query = """SELECT * FROM ninjas
    #                 WHERE id = %(ninja_id)s
    #             ;"""
    #     data = {"ninja_id": ninja_id}
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     ninja = cls(results[0])
    #     print (f"$$$$$$$$$$$$$$$$$ {ninja}")
    #     return ninja
    
    # Update Ninjas Models

    # @classmethod
    # def update(cls, data):
    #     query = """UPDATE ninjas
    #                 SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
    #                 WHERE id = %(ninja_id)s
    #             ;"""
    #     data = {
    #         "first_name": data['first_name'],
    #         "last_name": data['last_name'],
    #         "age": data['age'],
    #         "ninja_id": data['ninja_id']
    #     }
    #     connectToMySQL(cls.db).query_db(query, data)
    #     return

    # Delete Ninjas Models

    # @classmethod
    # def delete(cls, ninja_id):
    #     query = """ DELETE FROM ninjas
    #                 WHERE id = %(ninja_id)s
    #             ;"""
    #     data = {"ninja_id": ninja_id,
    #         }
    #     return connectToMySQL(cls.db).query_db(query, data)