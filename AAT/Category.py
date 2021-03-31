"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 07/12/2020

"""

import Dictionaries as Dct


class Category:
    def __init__(self, cat_id, cat_name):
        self.cat_id = cat_id
        self.cat_name = cat_name

    def add_cat(self):
        Dct.category[self.cat_id] = self.cat_name

    def edit_cat(self, cat_id, cat_name):
        Dct.category[self.cat_id] = cat_id
        Dct.category[self.cat_name] = cat_name

    def delete_cat(self, cat_id):
        Dct.category.discard[self.cat_id] = cat_id
