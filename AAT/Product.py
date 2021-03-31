"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 07/12/2020

"""

import Dictionaries as Dct


class Product:
    def __init__(self, prod_code, prod_name, prod_price):
        self.prod_code = prod_code
        self.prod_name = prod_name
        self.price = prod_price

    def add_prod(self):
        Dct.product[self.prod_code] = self.prod_name

    def edit_prod(self, prod_code, prod_name):
        Dct.product[self.prod_code] = prod_code
        Dct.product[self.prod_name] = prod_name

    def delete_prod(self, prod_code):
        Dct.product.discard[self.prod_code] = prod_code
