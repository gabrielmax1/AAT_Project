"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 27/01/2021
Python Coursework, AAT application, Features 1
"""

from Database import *
from tkinter import *

aat.conn_cat()
aat.conn_prod()
aat.conn_user()


# Submit Function for Database

def submit():
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()

    # Insert into table

    c.execute("INSERT INTO Products VALUES (:prod_id, :prod_name, :prod_desc, :prod_price, :prod_quantity, :prod_date)",
              {
                  'prod_id': prod_id.get(),
                  'prod_name': prod_name.get(),
                  'prod_desc': prod_desc.get(),
                  'prod_price': prod_price.get(),
                  'prod_quantity': prod_quantity.get(),
                  'prod_date': prod_date.get()
              })

    conn.commit()
    conn.close()

    # Clear text boxes first
    prod_id.delete(0, END)
    prod_name.delete(0, END)
    prod_desc.delete(0, END)
    prod_price.delete(0, END)
    prod_quantity.delete(0, END)
    prod_date.delete(0, END)


def show_stock_prod():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT * FROM Products")
    stock = c.fetchall()
    print_stock = ''
    for i in stock:
        # print_stock += str(i[]) + '\n'
        print_stock += str(i[1]) + " " + str(i[4]) + '\n'
    stock_queryl = Label(editor, text=print_stock)
    stock_queryl.grid(row=9, column=0, columnspan=2)


def select_all_prod():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT * FROM Products")
    records = c.fetchall()
    # print(records)
    # Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
        # If we wanna print only first two records of the entries(rows)
    # print_records += str(record[0]) + " " + str(record[1]) + '\n'
    query_label = Label(editor, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()
    conn.close()
    return


editor = Toplevel(root, title='AllAToys Database')
# data_window.title('AllAToys Database')

# Entry
prod_id = Entry(editor, width=20)
prod_id.grid(row=0, column=1, padx=20)
prod_name = Entry(editor, width=20)
prod_name.grid(row=1, column=1, padx=20)
prod_desc = Entry(editor, width=20)
prod_desc.grid(row=2, column=1, padx=20)
prod_price = Entry(editor, width=20)
prod_price.grid(row=3, column=1, padx=20)
prod_quantity = Entry(editor, width=20)
prod_quantity.grid(row=4, column=1, padx=20)
prod_date = Entry(editor, width=20)
prod_date.grid(row=5, column=1, padx=20)

# Text Box Labels
prod_id_l = Label(editor, text="Product code:")
prod_id_l.grid(row=0, column=0)
prod_name_l = Label(editor, text='Product Name')
prod_name_l.grid(row=1, column=0)
prod_desc_l = Label(editor, text='Product Desc:')
prod_desc_l.grid(row=2, column=0)
prod_price_l = Label(editor, text='Product Price')
prod_price_l.grid(row=3, column=0)
prod_quantity_l = Label(editor, text='Product Quantity')
prod_quantity_l.grid(row=4, column=0)
prod_date_l = Label(editor, text='Product Date')
prod_date_l.grid(row=5, column=0)

submit_btn = Button(editor, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(editor, text='Show records', command=select_all_prod)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=110)

show_stock_btn = Button(editor, text='Show me the Stock', command=show_stock_prod)
show_stock_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=120)
# Create a delete botton

delete_btn = Button(editor, text='Delete Record', command=delete_prod)
delete_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=110)

update_btn = Button(editor, text='Update Record', command=edit_prod)
update_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=110)


def delete_prod():
    global delete_prod
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("DELETE FROM Products WHERE prod_id=Prod_id")
    info = c.fetchall()

    conn.commit()
    conn.close()


def update_prod():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    items = prod_id.get()
    # Query the database
    c.execute("""UPDATE Products SET 
             ID = :id,
             Name = :name,
             Description = :desc,
             Price = :price,
             Quantity = :quantity,
             DataAdd = :date
             
             WHERE oid = :oid""",
              {'id': prod_id_editor.get(),
               'name': prod_name_editor.get(),
               'desc': prod_desc_editor.get(),
               'price': prod_desc_editor.get(),
               'quantity': prod_quantity_editor.get(),
               'date': prod_date_editor.get(),

               'oid': items
               }
              )
    info = c.fetchall()

    # Commit the changes in the Database.
    conn.commit()
    # Close the connection once done.
    conn.close()

    editor.destroy()


def edit_prod():
    global edit_prod, editor
    editor = Tk()
    editor.title('Edit the record selected.')
    editor.geometry("500x500")
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    items = prod_name.get()
    # Query the database
    c.execute("SELECT * FROM Products WHERE Name = " + items)
    info = c.fetchall()
    # Creating Global variables for text box names
    global prod_id_editor, prod_name_editor, prod_desc_editor, prod_price_editor, prod_quantity_editor, prod_date_editor
    # Entry
    prod_id_editor = Entry(editor, width=20)
    prod_id_editor.grid(row=0, column=1, padx=20)
    prod_name_editor = Entry(editor, width=20)
    prod_name_editor.grid(row=1, column=1, padx=20)
    prod_desc_editor = Entry(editor, width=20)
    prod_desc_editor.grid(row=2, column=1, padx=20)
    prod_price_editor = Entry(editor, width=20)
    prod_price_editor.grid(row=3, column=1, padx=20)
    prod_quantity_editor = Entry(editor, width=20)
    prod_quantity_editor.grid(row=4, column=1, padx=20)
    prod_date_editor = Entry(editor, width=20)
    prod_date_editor.grid(row=5, column=1, padx=20)

    # Text Box Labels
    prod_id_label = Label(editor, text="Product code:")
    prod_id_label.grid(row=0, column=0)
    prod_name_label = Label(editor, text='Product Name')
    prod_name_label.grid(row=1, column=0)
    prod_desc_label = Label(editor, text='Product Desc:')
    prod_desc_label.grid(row=2, column=0)
    prod_price_label = Label(editor, text='Product Price')
    prod_price_label.grid(row=3, column=0)
    prod_quantity_label = Label(editor, text='Product Quantity')
    prod_quantity_label.grid(row=4, column=0)
    prod_date_label = Label(editor, text='Product Date')
    prod_date_label.grid(row=5, column=0)

    # Loop thru the results
    for i in info:
        prod_id_editor.insert(0, i[0])
        prod_name_editor.insert(0, i[1])
        prod_desc_editor.insert(0, i[2])
        prod_price_editor.insert(0, i[3])
        prod_quantity_editor.insert(0, i[4])
        prod_date_editor.insert(0, i[5])

    save_btn = Button(editor, text='Save Record', command=update_prod)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=110)

# data_window.mainloop()
