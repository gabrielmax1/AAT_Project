"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 09/11/2020

"""
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox

db_uid = {'Gabriele': '12345',
          'Jack': '0000',
          'Diego': 'qwerty'}


def center_window():
    width, height = 250, 250  # Set the width and height
    screen_width = window.winfo_screenwidth()  # Get the screen width
    screen_height = window.winfo_screenheight()  # Get the screen height
    x_cord = int((screen_width / 2) - (width / 2))
    y_cord = int((screen_height / 2) - (height / 2))
    window.geometry("{}x{}+{}+{}".format(width,
                                         height,
                                         x_cord,
                                         y_cord))


def get_cred(input_username, input_password):
    input_username = username_entry.get()
    input_password = password_entry.get()


    def valid_login(username, password):
        if username == db_uid[password] and input_username == username and input_password == password:
            messagebox.showinfo('Info', 'Welcome back!')
        else:
            messagebox.showerror('Error', 'Invalid Login')


# GUI for the login
window = Tk()
window.title('All About Toys Login')
window.iconphoto(True, PhotoImage(file='windows_xp_logo.png'))

login_frame = Frame(window)

# Username
username_label = Label(window, text='Username:')
username_label.pack(padx=15, pady=10)
username_entry = Entry(window, bd=2)
username_entry.pack(padx=15, pady=10)

# Password
password_label = Label(window, text='Password: ')
password_label.pack(padx=15, pady=10)
password_entry = Entry(window, bd=2, show='*')
password_entry.pack(padx=15, pady=10)

login_btn = Button(login_frame, text='Login', bg='lightblue', command=get_cred)

login_btn.pack(side=RIGHT, padx=5)
login_frame.pack(padx=100, pady=19)

center_window()
window.mainloop()
