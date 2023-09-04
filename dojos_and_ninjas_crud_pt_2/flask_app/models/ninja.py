
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Ninja:
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Ninjas Models

    @classmethod
    def save(cls, data):
        query = """ INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at,        dojo_id)
                    VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s)
                ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    # Read Ninjas Models

    @classmethod
    def get_ninja_by_id(cls, ninja_id):
        query = """SELECT * FROM ninjas
                    WHERE id = %(ninja_id)s
                ;"""
        data = {"ninja_id": ninja_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        ninja = cls(results[0])
        print (f"$$$$$$$$$$$$$$$$$ {ninja}")
        return ninja
    
    # Update Ninjas Models

    @classmethod
    def update(cls, data):
        query = """UPDATE ninjas
                    SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
                    WHERE id = %(ninja_id)s
                ;"""
        data = {
            "first_name": data['first_name'],
            "last_name": data['last_name'],
            "age": data['age'],
            "ninja_id": data['ninja_id']
        }
        connectToMySQL(cls.db).query_db(query, data)
        return

    # Delete Ninjas Models

    @classmethod
    def delete(cls, ninja_id):
        query = """ DELETE FROM ninjas
                    WHERE id = %(ninja_id)s
                ;"""
        data = {"ninja_id": ninja_id,
            }
        return connectToMySQL(cls.db).query_db(query, data)