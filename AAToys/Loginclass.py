"""
Author: Gabriele Cotigliani
StudentID: 001115137
Date: 09/11/2020

"""
import sqlite3
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
from PIL import ImageTk, Image
import tkinter.font as font  # This lets us use different fonts.


class Login:

    def __init__(self):
        self.login_window = Tk()
        self.login_window.title('All About Toys Login')
        self.login_window.iconphoto(True, PhotoImage(file='images/windows_xp_logo.png'))
        self.login_window.config(bg='#529EFF')
        self.login_frame = Frame(self.login_window)
        self.arial_bold = font.Font(family='Arial', weight='bold')
        self.user_db()
        self.gui()

    def center_window(self):
        width, height = 400, 400  # Set the width and height
        screen_width = self.login_window.winfo_screenwidth()  # Get the screen width
        screen_height = self.login_window.winfo_screenheight()  # Get the screen height
        x_cord = int((screen_width / 2) - (width / 2))
        y_cord = int((screen_height / 2) - (height / 2))
        self.login_window.geometry("{}x{}+{}+{}".format(width,
                                                        height,
                                                        x_cord,
                                                        y_cord))

    def user_db(self):
        self.connection = sqlite3.connect("AllAToys.db")
        self.cursor = self.connection.cursor()
        '''
        self.cursor.execute(
            'CREATE TABLE if not exists Users ( Username varchar (18), Password varchar(30)'
            ' NOT NULL, account type varchar(7) NOT NULL, PRIMARY KEY(Username));')
        # self.cursor.execute('INSERT INTO Users VALUES ("Gabriele", "1234", "ADMIN")')
        '''

    # GUI for the login

    def gui(self):
        self.center_window()
        self.login_frame = LabelFrame(self.login_window, bg='White', height=300, width=300)
        self.login_frame.place(x=39, y=65)
        self.login_window.bind('<Return>', self.get_cred)
        self.arial_font = font.Font(family='Arial')
        self.comicsans_font = font.Font(family='Comic Sans')
        self.head_label = Label(self.login_frame, fg='#2FA200', bg='White', font=(self.arial_bold, 18),
                                text='Please insert your credential', anchor='center')
        self.head_label.pack(padx=5, pady=3)

        # Username
        self.username_label = Label(self.login_frame, text='Username: ', font=self.comicsans_font, bg='White')
        self.username_label.pack(padx=15, pady=10)
        self.username_entry = Entry(self.login_frame, bd=2, font=self.arial_font)
        self.username_entry.pack(padx=15, pady=10)

        # Password
        self.password_label = Label(self.login_frame, text='Password: ', font=self.comicsans_font, bg='White')
        self.password_label.pack(padx=15, pady=10)
        self.password_entry = Entry(self.login_frame, font=self.arial_font, bd=2, show='*')
        self.password_entry.pack(padx=15, pady=10)
        self.login_btn = Button(self.login_frame, width=10, text='Login', bg='#00D1D1', fg='black',
                                command=self.get_cred)
        self.login_btn.pack(padx=5)

    def get_cred(self, event=0):
        user_input = self.username_entry.get()
        pass_input = self.password_entry.get()
        self.connection = sqlite3.connect("AllAToys.db")
        self.cursor.execute('SELECT * FROM Users WHERE Username = ? and Password = ?', (user_input, pass_input))
        char = self.cursor.fetchall()
        if (len(char) > 0):
            self.valid_login()
        else:
            self.non_valid_login()
        return

    # If credentials True

    def valid_login(self):
        messagebox.showinfo('Info', 'Welcome back!')
        self.login_window.destroy()
    # else

    def non_valid_login(self):
        messagebox.showerror('Error', 'Invalid Login credentials. Check that it is correct.')
        self.login_window.focus()

    def register_user(self):
        self.head_label.config(text="Registration")
        self.head_label.place(x=40, y=25)

        self.login_btn.config(text="Ok", command=self.add_user)
        # ADD
        self.register_btn = Button(self.login_frame, width=20, text="Back", bg="lightblue2", fg="dimgray",
                                   command=self.re_do, font="Roboto 14")
        self.register_btn.place(x=35, y=320)
        self.register_btn.config(text="Back", command=self.re_do)
        self.login_btn.config()
        self.login_btn.place(x=35, y=260)
        self.password_entry.config(show='*')

        self.login_window.focus()
        self.login_window.bind('<Esc>', self.login_window.destroy())
        self.login_window.bind('<Return>', self.add_user)
        self.login_window.title('Register')

        # Adding Account User to Database

    def add_user(self, event=0):
        self.login_window.bind('<Esc>', self.login_window.destroy())
        user_input = self.username_entry.get()
        pass_input = self.password_entry.get()

        self.cursor.execute('SELECT Username from Users WHERE Username = ?', (user_input,))
        char = self.cursor.fetchall()
        if (len(char) > 0):
            messagebox.showerror("Error", "Username already exist")
            self.login_window.focus()
            return
        if (len(user_input) == 0 or len(user_input) > 18):
            messagebox.showerror('Error', 'Invalid Username format, max 18 characters, min 1')
            # self.username.set('Please choose another Username')
            self.login_window.focus()
            return
        if (len(pass_input) == 0 or len(pass_input) > 30 or len(pass_input) < 6):
            messagebox.showerror('Please create a valid Password, max 30 characters, min 6\n'
                                 'For a strong Password, try to use Upper, lower case\n'
                                 'Special char. #$&, and Numbers 67391')
            self.password_entry.config(show='*')
            self.login_window.focus()
            return
        else:
            self.cursor.execute('INSERT INTO Users VALUES(?, ?, ?)', (user_input, pass_input, 'USER'))
            messagebox.showinfo('Success', 'User successfully added to the system')
            self.connection.commit()
            self.re_do()
            self.login_window.state('withdraw')
            self.tree.delete(*self.tree.get_children())
            self.getAccounts()

    def re_do(self):
        self.head_label.config(text="Login")
        self.head_label.place(x=75, y=25)
        self.login_btn.config(text="Sign in", command=self.get_cred)
        self.register_btn.config(text="Register", command=self.register_user)

        self.password_entry.config(show='*')
        self.login_btn.config(state=NORMAL)
        self.login_window.focus()

        self.login_window.bind('<Return>', self.get_cred())
        self.login_window.bind('<Esc>', self.login_window.destroy())
        self.login_btn.place(x=35, y=290)
        self.login_window.title('Login')
        self.login_window.state('withdraw')

    def __quit__(self):
        if messagebox.askyesno('Quit', 'Do you wanna quit the program?'):
            self.login_window.destroy()
            exit(0)


# log_in = Login()

if __name__ == '__main__':
    r = Login()
    r.connection.commit()
    r.login_window.mainloop()
