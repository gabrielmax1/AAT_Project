"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 07/12/2020
Python Coursework, AAT application, Features 1
"""
import tkinter as tk  # This has all the code for GUIs.
from tkinter import *
import tkinter.font as font  # This lets us use different fonts.
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
import Category as Cat
import Product as Prod
import Dictionaries as Dct
import Functions as fnc


def login_page():
    def center_login_window():
        width, height = 250, 250  # Set the width and height
        screen_width = login_window.winfo_screenwidth()  # Get the screen width
        screen_height = login_window.winfo_screenheight()  # Get the screen height
        x_cord = int((screen_width / 2) - (width / 2))
        y_cord = int((screen_height / 2) - (height / 2))
        login_window.geometry("{}x{}+{}+{}".format(width,
                                                   height,
                                                   x_cord,
                                                   y_cord))

    def valid_login():
        if username_entry.get() in Dct.admin_credentials.keys():
            if Dct.admin_credentials[username_entry.get()] == password_entry.get():
                messagebox.showinfo('Info', 'Welcome back!')
                login_window.destroy()
                loginbtn.place_forget()
                label_home.place_forget()
                top_frame_btn()
                search_bar()
            else:
                messagebox.showerror('Error', 'Invalid Password')
        else:
            messagebox.showerror('Error', 'Invalid Username credentials, Username is case sensitive.')

    # GUI for the login
    login_window = Tk()
    login_window.title('All About Toys Login Window')
    # login_window.iconphoto(True, PhotoImage(file='windows_xp_logo.png'))

    login_frame = Frame(login_window)

    # Username
    username_label = Label(login_window, text='Username:')
    username_label.pack(padx=15, pady=10)
    username_entry = Entry(login_window, bd=2)
    username_entry.pack(padx=15, pady=10)

    # Password
    password_label = Label(login_window, text='Password: ')
    password_label.pack(padx=15, pady=10)
    password_entry = Entry(login_window, bd=2, show='*')
    password_entry.pack(padx=15, pady=10)

    login_btn = Button(login_frame, text='Login', bg='lightblue', command=valid_login)

    login_btn.pack(side=RIGHT, padx=5)
    login_frame.pack(padx=100, pady=19)

    center_login_window()
    login_window.mainloop()


# GUI for my top frame containing the buttons that they will call functionalities
def top_frame_btn():
    topframe = tk.Frame(root, bg='#80c1ff', bd=4)
    topframe.place(relx=0, rely=0, relwidth=1, relheight=0.07)

    change_user_btn = tk.Button(topframe, text='Change User', font=arial, bg='white', fg='blue', command=login_page)
    change_user_btn.place(relx=0, rely=0, relwidth=0.12, relheight=0.8)

    product_btn = tk.Button(topframe, text='Products', font=arial, bg='white', fg='blue')
    product_btn.place(relx=0.14, rely=0, relwidth=0.1, relheight=0.8)

    category_btn = tk.Button(topframe, text='Categories', font=arial, bg='white', fg='blue', )
    category_btn.place(relx=0.26, rely=0, relwidth=0.1, relheight=0.8)

    settings_btn = tk.Button(topframe, text='Settings', font=arial, bg='white', fg='blue')
    settings_btn.place(relx=0.38, rely=0, relwidth=0.1, relheight=0.8)

    exit_btn = tk.Button(topframe, text='Exit', font=arial, bg='white', fg='blue', command=quit)
    exit_btn.place(relx=0.50, rely=0, relwidth=0.1, relheight=0.8)


# This will be my search bar.
def search_bar():
    search_frame = tk.Frame(root, bg='#80c1ff', bd=5)
    search_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.08, anchor='n')

    search_entry = tk.Entry(search_frame, bg='lightgreen', bd=2)
    search_entry.place(relwidth=0.65, relheight=1)

    button1 = tk.Button(search_frame, bg='white', fg='blue', activebackground='blue', activeforeground='white',
                        text="<-- Search", font='40', command=fnc.search_prod_by_name)
    button1.place(relx=0.7, rely=0, relwidth=0.15, relheight=1)

    # lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    # lower_frame.place(relx=0.2, rely=0.55, relwidth=0.5, relheight=0.4)


# label1 = tk.Label(lower_frame)
# label1.place(relwidth=1, relheight=1)


root = tk.Tk()
root.title("All About Toys Online Store")  # The text in the title bar
root.iconphoto(True, tk.PhotoImage(file='windows_xp_logo.png'))  # The icon logo, top left in the bar

# Giving a specific size to my window at start
height = 550
width = 1200

canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()
root.configure(bg='#80c1ff')

toys_background = ImageTk.PhotoImage(
    Image.open("C:\\Users\\mix__\\Desktop\\Uni\\COMP1811 Paradigms of Programming\\CW\\Py\\real_toys.png"))
background_home = tk.Label(root, image=toys_background)
background_home.place(relheight=1, relwidth=1)

arial = font.Font(family='Arial', weight='bold')
home_font = font.Font(family='Comic Sans MS', size='20', weight='bold')
label_home = tk.Label(root, text='Welcome to our Online Store\n'
                                 'Please login, to access exclusive content.',
                      font=home_font,
                      bg='white', fg='green')
label_home.place(rely=0.15, relx=0.2, relheight=0.25, relwidth=0.6)

# Main Login botton \\\\\\\\\\

loginbtn = tk.Button(root, text='Login', font=arial, bg='white', fg='blue', command=login_page)
loginbtn.place(relx=0.45, rely=0.65, relwidth=0.08, relheight=0.08)

# \\\\\\\\\\\\\\\\\\\\\


root.mainloop()
