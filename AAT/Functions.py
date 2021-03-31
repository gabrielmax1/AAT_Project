"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 07/12/2020

"""
import User as usr
import Product as Prod
import Category as Cat
import Dictionaries as Dct


# In this .py I will list all of my functions.
def search_prod_by_name():
    prod_name = input(str('Insert the product Name : '))
    if prod_name in Dct.product.values():
        print(prod_name)
    else:
        print('We could not find the product, try searching with product code.')
# For now this function works as a test, meaning that the button "Search" will run it, but it will ask
# A prompt input from the Python Run. I will change it so that it will reconise if it is a product or category.

def search_prod_by_code():
    prod_code = input(str('Insert the product Code : '))
    if prod_code in Dct.product.keys():
        print(prod_code)
    else:
        print('We could not find the product. :/ ')


def add_prod():
    prod_code = input(str('Insert the product Code : '))
    prod_name = input(str('Insert the product Name : '))
    new_prod = Prod.Product(prod_code, prod_name)
    new_prod.add_prod()


def update_prod():
    prod_code = input(str('Insert the actual product Code : '))
    if prod_code in Dct.product.keys():
        new_prod_name = input(str('Change name to : '))
        prod_name = new_prod_name
    else:
        print('We could not find the specific product, please double check the code.')
    Cat.Category.update_prod(prod_code, prod_name)


def delete_prod():
    prod_code = input(str('Insert the product code that you want to delete : '))
    prod_name = input(str('Insert the product name that you want to delete : '))
    if prod_code in Dct.product.keys() and prod_name in Dct.product.values():
        Dct.product.delete(prod_code, prod_name)
    else:
        print('We could not find the specific product, please double check the code.')
    Cat.Category.delete_prod(prod_code, prod_name)


def add_cat():
    cat_id = input(str('Insert the new category Id: '))
    cat_name = input(str('Insert the new category name : '))
    new_cat = Cat.Category(cat_id, cat_name)
    new_cat.add.cat()


def update_cat():
    cat_id = input(str('Insert the category Id you want to change : '))
    if cat_id in Dct.category.keys():
        cat_name = input(str('Insert the new category name : '))
    else:
        print('We could not find the category Id or name.')
    Cat.Category.edit_cat(cat_id, cat_name)


def delete_cat():
    cat_id = input(str('Insert the category Id you want to delete : '))
    cat_name = input(str('Insert the product name that you want to delete : '))
    if cat_id in Dct.category.keys() and cat_name in Dct.product.values():
        Dct.product.delete(cat_id, cat_name)
    else:
        print('We could not find the specific product, please double check the code.')
    Cat.Category.delete_prod(cat_id, cat_name)


def search_cat_prod_by_name():
    cat_name = input(str('Insert the category Name : '))
    if cat_name in Dct.category.values():
        print(cat_name)
    else:
        print('We could not find the category, try searching with category Id.')


def search_cat_by_id():
    cat_id = input(str('Insert the category Id : '))
    if cat_id in Dct.category.keys():
        print(cat_id)
    else:
        print('We could not find the category. :/ ')
