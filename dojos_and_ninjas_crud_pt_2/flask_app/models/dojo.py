
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models import ninja
# import re
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)
# The above is used when we do login registration, flask-bcrypt should already be in your env check the pipfile

# Remember 'fat models, skinny controllers' more logic should go in here rather than in your controller. Your controller should be able to just call a function from the model for what it needs, ideally.

class Dojo:
    db = "dojos_and_ninjas_schema" #which database are you using for this project
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        # What changes need to be made above for this project?
        #What needs to be added here for class association?



    # Create Dojos Models

    @classmethod
    def save(cls, data):
        query = """INSERT INTO dojos (name, created_at, updated_at)
                    VALUES (%(name)s, NOW(), NOW())
                ;"""
        return connectToMySQL(cls.db).query_db(query, data)

    # Read Dojos Models

    @classmethod
    def get_all_dojos(cls):
        query = """ SELECT * FROM dojos
                ;"""
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for one_dojo in results:
            dojos.append(cls(one_dojo))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        data = {
            "id": dojo_id
        }
        query = """SELECT * FROM dojos 
                    LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id 
                    WHERE dojos.id = %(id)s;"""
        results = connectToMySQL(cls.db).query_db(query, data)
        one_dojo = cls(results[0])
        for result in results:
            ninja_data = {
                'id': result['ninjas.id'],
                'first_name': result['first_name'],
                'last_name': result['last_name'],
                'age': result['age'],
                'created_at': result['ninjas.created_at'],
                'updated_at': result['ninjas.updated_at'],
                'dojo_id': result['dojo_id']
            }
            one_dojo.ninjas.append(ninja.Ninja(ninja_data))
        print (one_dojo.ninjas)
        return one_dojo

    # Update Dojos Models
    


    # Delete Dojos Models