# import sqlite3
from db import db

class ItemModel(db.Model):#inherit from sqlalchemy model
    '''Now sqlalchemy will create mappings from DB and the objects of this class
    We need to tell sqlalchemy the name of table that it will store these model'''
    __tablename__='items'
    id = db .Column(db.Integer,primary_key=True)
    name  = db.Column(db.String(50))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def json(self):
        return {'name':self.name,'price':self.price}

#this should remain  class method because it return obect of type item model as opposed to dicct earlier
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #select * from items where name = name

    def save_to_DB(self): # equivalent to update or insert
        db.session.add(self)
        db.session.commit()
    # def insert(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "INSERT INTO items VALUES(?, ?)"    
    #     cursor.execute(query, (self.name, self.price))

    #     connection.commit()
    #     connection.close()
    
    
    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.name, self.price))

    #     connection.commit()
    #     connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
