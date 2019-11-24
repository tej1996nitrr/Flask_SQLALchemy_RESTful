import sqlite3
'''This class is a helper class, it is not a resource
because api can't send or receive data(json) from this class
Model is our internal representaion of entity
Resource is an external representation of an entity
'''
from db import db

#this is an api that exposes two endpoints, findbyusername and findbyid
#And that includes writing it to a database
##and retrieving it from a database.
#security.py communicates with database using these endpoints
class UserModel(db.Model):

    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True) #id will be automatically assigned by sqlalchemy because it is primary key
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    TABLE_NAME = 'users'

    def __init__(self, username, password):
        # self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def find_by_username(cls, username):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (username,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row)
        # else:
        #     user = None

        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
