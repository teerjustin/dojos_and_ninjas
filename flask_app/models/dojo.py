from flask_app.config.mysqlconnection import connectToMySQL

from .ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['dojo_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"	        # call the function, passing in the name of our db
        dojos_from_database = connectToMySQL("dojos_and_ninjas").query_db(query)  # call the query_db function, pass in the query as a string
        return dojos_from_database
    
    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        
        dojo_obj = cls(results[0])
        print(dojo_obj, '==============================================')
        return dojo_obj

    # #create
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (dojo_name, created_at, updated_at)" \
        "VALUES (%(dojo_name)s, NOW(), NOW());"

        dojo_id = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return dojo_id

#show ninjas ON specific dojo
    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id " \
            "WHERE dojos.id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        print(results, '*************************************************')

        dojo = cls(results[0])
        print(dojo, 'zzzzzzzzzzzzzzzzzzzzzzzzzzz')

        for row in results:
            data = {
                "id": row['ninja_id'],
                "dojo_id": row['dojo_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }

            dojo.ninjas.append(Ninja(data))
        return dojo