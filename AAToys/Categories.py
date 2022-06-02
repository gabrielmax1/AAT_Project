"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 27/01/2021
Python Coursework, AAT application, Features 1
"""

import sqlite3
import Database as db


class Category:
    def __init__(self, cat_id, cat_name):
        self.id = cat_id
        self.name = cat_name


class Product(Category):
    def __init__(self, cat_id, prod_id, name, description, price, quantity, date):
        super().__init__(self, cat_id)
        self.id = prod_id
        self.name = name
        self.desc = description
        self.price = price
        self.quantity = quantity
        self.date = date
        self.load_prod()

    def __str__(self):
        return "Product: {}\nDescription: {}\nPrice: {} ".format(self.name, self.desc, self.price)

    def __repr__(self):
        return "{}(Product: {}, Description: {}, Price: {})".format(self.__class__.__name__, \
                                                                  self.name, self.desc, self.price)
    def load_prod(self):
        self.connection = sqlite3.connect("AllAToys.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM Products')
        fet_tching = self.cursor.fetchall()
        print(fet_tching)

    # def add_prod(self):


teddybear = Product('0001', '010001', 'Teddy', 'Plush Teddy little bear.', 12, 50, '03/01/2021')
barbiedoll = Product('0002', '010002', 'Barbie', 'Best seller doll for baby-girls.', 9, 30, '03/01/2021')
racingcar = Product('0003', '010003', 'Racing Car', 'Classic RC car for boys.', 18, 20, '03/01/2021')
legocity = Product('0004', '010004', 'Lego City', 'Build your own city.', 20, 19, '03/01/2021')

# print(teddybear)
