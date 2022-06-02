"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 27/01/2021
Python Coursework, AAT application, Features 1
"""
import tkinter as tk  # This has all the code for GUIs.
from tkinter import *
import tkinter.font as font  # This lets us use different fonts.
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
from Database import *


def log_in_window():
    def center_window():
        width, height = 380, 380  # Set the width and height
        screen_width = login_window.winfo_screenwidth()  # Get the screen width
        screen_height = login_window.winfo_screenheight()  # Get the screen height
        x_cord = int((screen_width / 2) - (width / 2))
        y_cord = int((screen_height / 2) - (height / 2))
        login_window.geometry("{}x{}+{}+{}".format(width,
                                                   height,
                                                   x_cord,
                                                   y_cord))

    def get_cred(event=0):
        conn = sqlite3.connect("AllAToys.db")
        c = conn.cursor()
        user_input = username_entry.get()
        pass_input = password_entry.get()
        char = c.execute('SELECT * FROM Users WHERE Username = ? and Password = ?', (user_input, pass_input))
        char = c.fetchall()
        if (len(char) > 0):
            messagebox.showinfo('Info', 'Welcome back!')
            login_window.destroy()
            label_home.place_forget()
            log_in_btn.place_forget()
            top_frame_btn()
            # search_bar()

        else:
            messagebox.showerror('Error', 'Invalid Login credentials. Check that it is correct.')
            login_window.focus()
        return

    # GUI for the login
    login_window = Tk()
    login_window.title('All About Toys Login')
    # login_window.iconphoto(True, PhotoImage(file='images/windows_xp_logo.png'))
    login_window.config(bg='#529EFF')
    login_frame = LabelFrame(login_window, bg='White', height=300, width=300)
    login_frame.place(x=60, y=65)
    login_window.bind('<Return>', get_cred)
    head_label = Label(login_frame, fg='#2FA200', bg='White', font='arial',
                       text='Please insert your credential', anchor='center')
    head_label.pack(padx=5, pady=3)

    # Username
    username_label = Label(login_frame, text='Username: ', font=comicsans_font, bg='White')
    username_label.pack(padx=15, pady=10)
    username_entry = Entry(login_frame, bd=2, font=arial_font)
    username_entry.pack(padx=15, pady=10)

    # Password
    password_label = Label(login_frame, text='Password: ', font=comicsans_font, bg='White')
    password_label.pack(padx=15, pady=10)
    password_entry = Entry(login_frame, font=arial_font, bd=2, show='*')
    password_entry.pack(padx=15, pady=10)
    login_btn = Button(login_frame, width=10, text='Login', bg='#00D1D1', fg='black',
                       command=get_cred)
    login_btn.pack(padx=5)
    center_window()
    login_window.mainloop()


# GUI for my top frame containing the buttons that they will call functionalities
def top_frame_btn():
    topframe = tk.Frame(home_window, bg='#80c1ff', bd=4)
    topframe.place(relx=0, rely=0, relwidth=1, relheight=0.07)

    change_user_btn = tk.Button(topframe, text='Change User', font=arial_font, bg='white', fg='blue',
                                command=log_in_window)
    change_user_btn.place(relx=0, rely=0, relwidth=0.12, relheight=0.8)

    product_btn = tk.Button(topframe, text='Products', font=arial_font, bg='white', fg='blue', command=call_prod_gui)
    product_btn.place(relx=0.14, rely=0, relwidth=0.1, relheight=0.8)

    category_btn = tk.Button(topframe, text='Categories', font=arial_font, bg='white', fg='blue', command=call_cat_gui)
    category_btn.place(relx=0.26, rely=0, relwidth=0.1, relheight=0.8)

    settings_btn = tk.Button(topframe, text='Settings', font=arial_font, bg='white', fg='blue')
    settings_btn.place(relx=0.38, rely=0, relwidth=0.1, relheight=0.8)

    exit_btn = tk.Button(topframe, text='Exit', font=arial_font, bg='white', fg='blue', command=quit)
    exit_btn.place(relx=0.50, rely=0, relwidth=0.1, relheight=0.8)


# This will be my search bar.
def search_bar():
    search_frame = tk.Frame(home_window, bg='#80c1ff', bd=5)
    search_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.08, anchor='n')

    search_entry = tk.Entry(search_frame, bg='lightgreen', bd=2)
    search_entry.place(relwidth=0.65, relheight=1)

    button1 = tk.Button(search_frame, bg='white', fg='blue', activebackground='blue', activeforeground='white',
                        text="<-- Search", font='40', command='')
    button1.place(relx=0.7, rely=0, relwidth=0.15, relheight=1)

    lower_frame_src = tk.LabelFrame(home_window, bg='White', bd=5)
    lower_frame_src.place(relx=0.2, rely=0.58, relwidth=0.65, relheight=0.4)


# ================================ Products GUI ============================================

def call_prod_gui():
    data_frame = LabelFrame(home_window, bg="White", bd=2)
    data_frame.place(relx=0.2, rely=0.15, relwidth=0.3, relheight=0.4)

    btn_frame = LabelFrame(home_window, bg='White', bd=2)
    btn_frame.place(relx=0.56, rely=0.15, relwidth=0.29, relheight=0.4)
    global lower_frame
    lower_frame = tk.LabelFrame(home_window, bg='White', bd=2)
    lower_frame.place(relx=0.2, rely=0.58, relwidth=0.65, relheight=0.38)

    # =============== Products Entries Gui ==================

    global prod_id, prod_name, prod_desc, prod_price, prod_quantity, prod_date
    prod_id = Entry(data_frame, width=20, bd=2)
    prod_id.grid(row=0, column=1, padx=20, pady=(10, 0))
    prod_name = Entry(data_frame, width=20, bd=2)
    prod_name.grid(row=1, column=1, padx=20)
    prod_desc = Entry(data_frame, width=20, bd=2)
    prod_desc.grid(row=2, column=1, padx=20)
    prod_price = Entry(data_frame, width=20, bd=2)
    prod_price.grid(row=3, column=1, padx=20)
    prod_quantity = Entry(data_frame, width=20, bd=2)
    prod_quantity.grid(row=4, column=1, padx=20)
    prod_date = Entry(data_frame, width=20, bd=2)
    prod_date.grid(row=5, column=1, padx=20)
    # Text Box Labels
    prod_id_l = Label(data_frame, text="Product Code:", bg='White')
    prod_id_l.grid(row=0, column=0, pady=(10, 0))
    prod_name_l = Label(data_frame, text='Product Name', bg='White')
    prod_name_l.grid(row=1, column=0)
    prod_desc_l = Label(data_frame, text='Product Desc:', bg='White')
    prod_desc_l.grid(row=2, column=0)
    prod_price_l = Label(data_frame, text='Product Price', bg='White')
    prod_price_l.grid(row=3, column=0)
    prod_quantity_l = Label(data_frame, text='Product Quantity', bg='White')
    prod_quantity_l.grid(row=4, column=0)
    prod_date_l = Label(data_frame, text='Product Date', bg='White')
    prod_date_l.grid(row=5, column=0)
    # =============================== Buttons ========================================
    add_btn = Button(data_frame, text="Add Record into Database", command=add_prod, bg='#F58D00', fg='black')
    add_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=60)

    print_btn = Button(btn_frame, text='Show Records', bg='#00D1D1', fg='black', command=print_all_prod)
    print_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=70)

    show_stock_btn = Button(btn_frame, text='Show the Stock', bg='#278820', fg='black', command=show_stock_prod)
    show_stock_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10, ipadx=65)

    clear_btn = Button(btn_frame, text='Clear', bg='#0015E8', fg='white', command=clear_label)
    clear_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

    update_btn = Button(btn_frame, text='Edit Record', command=edit_prod, bg='#1CADA2', fg='black')
    update_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=72)

    delete_btn = Button(data_frame, text='Delete Record', command=delete_prod, bg='#D61313', fg='black')
    delete_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=70)


# ============================== Product Functions =========================================

# Add a product to the database
def add_prod():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    # Insert into table

    c.execute(
        "INSERT INTO Products VALUES (:prod_id, :prod_name, :prod_desc, :prod_price, :prod_quantity, :prod_date)",
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
               'price': prod_price_editor.get(),
               'quantity': prod_quantity_editor.get(),
               'date': prod_date_editor.get(),

               'oid': items
               }
              )

    # Commit the changes in the Database.
    conn.commit()
    # Close the connection once done.
    conn.close()

    editor.destroy()


def edit_prod():
    global edit_prod, editor
    editor = Tk()
    editor.title('Edit the Record selected.')
    editor.geometry('300x250')
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    items = prod_id.get()
    # Query the database
    c.execute("SELECT * FROM Products WHERE ID = " + items)
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

    save_btn = Button(editor, text='Save Record', command=update_prod, bg='#1CAC30', fg='black')
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=90)


# Delete a product from the database, will be use the same Entry as for add, prod_name.
def delete_prod():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("DELETE FROM Products WHERE Name = :prod_name",
              {
                  'prod_name': prod_name.get()
              })
    conn.commit()
    conn.close()
    prod_name.delete(0, END)


# This will Print out the actual stock take on the products.

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
    global stock_query
    stock_query = Label(lower_frame, text=print_stock, bg='White')
    stock_query.grid(row=9, column=0, columnspan=2, ipadx=120, ipady=10)
    conn.commit()
    conn.close()


# This will Print out the tuples from each row in the database.
def print_all_prod():
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
    global query_label
    query_label = Label(lower_frame, text=print_records, bg='White')
    query_label.grid(row=8, column=0, columnspan=2, ipadx=100, ipady=20)

    conn.commit()
    conn.close()
    return


# This is just to clean the LabelFrame where all the info are displayed on command.
def clear_label():
    stock_query.grid_forget()
    query_label.grid_forget()


# ===================== Category GUI ==============================

def call_cat_gui():
    data_frame = LabelFrame(home_window, bg="White", bd=2)
    data_frame.place(relx=0.2, rely=0.15, relwidth=0.3, relheight=0.4)

    btn_frame = LabelFrame(home_window, bg='White', bd=2)
    btn_frame.place(relx=0.56, rely=0.15, relwidth=0.29, relheight=0.4)
    global lower_frame
    lower_frame = tk.LabelFrame(home_window, bg='White', bd=2)
    lower_frame.place(relx=0.2, rely=0.58, relwidth=0.65, relheight=0.38)

    # =============== Category Entries Gui ==================

    global cat_id, cat_name, cat_date
    cat_id = Entry(data_frame, width=20, bd=2)
    cat_id.grid(row=0, column=1, padx=20, pady=(10, 0))
    cat_name = Entry(data_frame, width=20, bd=2)
    cat_name.grid(row=1, column=1, padx=20)
    cat_date = Entry(data_frame, width=20, bd=2)
    cat_date.grid(row=2, column=1, padx=20)
    # Text Box Labels
    cat_id_l = Label(data_frame, text="Category Code:", bg='White')
    cat_id_l.grid(row=0, column=0, pady=(10, 0))
    cat_name_l = Label(data_frame, text='Category Name', bg='White')
    cat_name_l.grid(row=1, column=0)
    cat_date_l = Label(data_frame, text='Category Date:', bg='White')
    cat_date_l.grid(row=2, column=0)

    # ======================= Buttons ===============================

    add_btn = Button(data_frame, text="Add Category into Database", command=add_cat, bg='#F58D00', fg='black')
    add_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=70)

    print_btn = Button(btn_frame, text='Print Categories', bg='#00D1D1', fg='black', command=print_all_cat)
    print_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, ipadx=90)

    delete_btn = Button(data_frame, text='Delete Category', command=delete_cat, bg='#D61313', fg='black')
    delete_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    clear_btn = Button(btn_frame, text='Clear', bg='#0015E8', fg='white', command=clr_cat_label)
    clear_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=115)

    update_btn = Button(data_frame, text='Edit Record', command=edit_cat, bg='#1CADA2', fg='black')
    update_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)


# This will add a category to the database Category

def add_cat():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    # Insert into table

    c.execute(
        "INSERT INTO Category VALUES (:cat_id, :cat_name, :cat_date)",
        {
            'cat_id': cat_id.get(),
            'cat_name': cat_name.get(),
            'cat_date': cat_date.get()

        })

    conn.commit()
    conn.close()

    # Clear text boxes first
    cat_id.delete(0, END)
    cat_name.delete(0, END)
    cat_date.delete(0, END)


def update_cat():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    items = cat_id.get()
    # Query the database
    c.execute("""UPDATE Category SET 
             ID = :id,
             Name = :name,
             DataAdd = :date

             WHERE oid = :oid""",
              {'id': cat_id_editor.get(),
               'name': cat_name_editor.get(),
               'date': cat_date_editor.get(),

               'oid': items
               }
              )

    # Commit the changes in the Database.
    conn.commit()
    # Close the connection once done.
    conn.close()

    editor.destroy()


def edit_cat():
    global edit_cat, editor
    editor = Tk()
    editor.title('Edit the Category selected.')
    editor.geometry('300x250')
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    items = cat_id.get()
    # Query the database
    c.execute("SELECT * FROM Category WHERE ID = " + items)
    info = c.fetchall()
    # Creating Global variables for text box names
    global cat_id_editor, cat_name_editor, cat_date_editor
    # Entry
    cat_id_editor = Entry(editor, width=20)
    cat_id_editor.grid(row=0, column=1, padx=20)
    cat_name_editor = Entry(editor, width=20)
    cat_name_editor.grid(row=1, column=1, padx=20)
    cat_date_editor = Entry(editor, width=20)
    cat_date_editor.grid(row=2, column=1, padx=20)

    # Text Box Labels
    cat_id_label = Label(editor, text="Category Code:")
    cat_id_label.grid(row=0, column=0)
    cat_name_label = Label(editor, text='Category Name')
    cat_name_label.grid(row=1, column=0)
    cat_date_label = Label(editor, text='Category Date')
    cat_date_label.grid(row=2, column=0)

    # Loop thru the results
    for i in info:
        cat_id_editor.insert(0, i[0])
        cat_name_editor.insert(0, i[1])
        cat_date_editor.insert(0, i[2])

    save_btn = Button(editor, text='Save Category', command=update_cat, bg='#1CAC30', fg='black')
    save_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, ipadx=90)


def delete_cat():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("DELETE FROM Category WHERE Name = :cat_name",
              {
                  'cat_name': cat_name.get()
              })
    conn.commit()
    conn.close()
    cat_name.delete(0, END)


# Print all the Categories inside the database

def print_all_cat():
    # Connect to the database
    conn = sqlite3.connect('AllAToys.db')
    c = conn.cursor()
    # Query the database
    c.execute("SELECT * FROM Category")
    lists = c.fetchall()
    # print(records)
    # Loop Thru Results
    print_records = ''
    for list in lists:
        print_records += str(list) + '\n'
        # If we wanna print only first two records of the entries(rows)
    # print_records += str(record[0]) + " " + str(record[1]) + '\n'
    global query_label
    query_label = Label(lower_frame, text=print_records, bg='White')
    query_label.grid(row=8, column=0, columnspan=2, ipadx=120, ipady=20)

    conn.commit()
    conn.close()
    return


# This will clean the LabelFrame where all the information are printed on command.
def clr_cat_label():
    query_label.grid_forget()


# =========================== Root GUI =======================================
root = tk.Tk()
root.title("All About Toys Online Store")  # The text in the title bar
root.iconphoto(True, PhotoImage(file='images/windows_xp_logo.png'))  # The icon logo, top left in the bar

# Giving a specific size to my window at start
height = 550
width = 1200

home_window = root
canvas = tk.Canvas(home_window, height=height, width=width)
canvas.pack()
home_window.configure(bg='#80c1ff')

img_background = ImageTk.PhotoImage(Image.open("images/toys_image.png"))
background_home = tk.Label(home_window, image=img_background)
background_home.place(relheight=1, relwidth=1)

arial_font = font.Font(family='Arial')
comicsans_font = font.Font(family='Comic Sans')
arial_bold = font.Font(family='Arial', weight='bold')
home_font = font.Font(family='Comic Sans MS', size='20', weight='bold')
label_home = tk.Label(home_window, text='Welcome to our Online Store\n'
                                        'Please login, to access exclusive content.',
                      font=home_font,
                      bg='white', fg='green')
label_home.place(rely=0.15, relx=0.2, relheight=0.25, relwidth=0.6)

log_in_btn = tk.Button(home_window, text='Login', font=arial_bold, bg='white', fg='blue', command=log_in_window)
log_in_btn.place(relx=0.45, rely=0.65, relwidth=0.08, relheight=0.08)

# ============================= Database Connection ===================================

aat.conn_cat()
aat.conn_prod()
aat.conn_user()

# ============= Fill database, if empty removes comments. ================
# aat.fill_prod()
# aat.fill_cat()
# aat.fill_user()


root.mainloop()
