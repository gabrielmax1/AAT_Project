import sqlite3


class DataBase(object):
    def __init__(self, file_name):
        self.file = file_name
        self.conn = sqlite3.connect(self.file)
        self.c = self.conn.cursor()

    # def __str__(self):
    #    return "Product: {}\nDescription: {}\nPrice: {} ".format(self.name, self.desc, self.price)

    def login(self, user_input, pass_input):
        self.c.execute('SELECT * FROM Users WHERE Username = ? and Password = ?', (user_input, pass_input))
        admin_users = self.c.fetchall()  # returns all the rows as a list of tuples
        self.conn.commit()
        self.conn.close()
        return admin_users

    def conn_prod(self):
        self.c.execute("CREATE TABLE if not exists Products (ID INTEGER PRIMARY KEY, Name varchar (20),"
                       " Description varchar(100), Price REAL NOT NULL, Quantity INTEGER NOT NULL, DateAdd DATETIME);")

    def conn_cat(self):
        self.c.execute("CREATE TABLE if not exists Category (ID INTEGER PRIMARY KEY, Name varchar(15) NOT NULL, "
                       "DataAdd DATETIME);")

    def conn_user(self):
        self.c.execute('CREATE TABLE if not exists Users ( Username varchar (18), Password varchar(30)'
                       ' NOT NULL, account type varchar(7) NOT NULL, PRIMARY KEY(Username));')

    def search(self):
        self.c.execute('SELECT * FROM Products')
        v = self.c.fetchall()
        self.conn.commit()
        self.conn.close()
        return v

    def search_prod_name(self):
        prod_name = input(str('Insert the product Name : '))
        self.c.execute("SELECT Name FROM Products WHERE Name= ?", (prod_name,))
        y = self.c.fetchall()
        print(y)

    def edit(self):
        self.c.execute()
        self.conn.commit()
        self.conn.close()

    def fill_prod(self):
        self.c.execute(
            'INSERT INTO Products VALUES ("000001", "Unicorn", "Soft and fluffy unicorn for children", "10.99", '
            '"50", "03/01/2021");')
        self.c.execute(
            'INSERT INTO Products VALUES ("000002", "Cicciobello", "The baby-girls favorites baby doll", "15",'
            '"50", "03/01/2021");')
        self.c.execute(
            'INSERT INTO Products VALUES ("000003", "Lego Police Car", "Classic lego bricks", "8.90","20", '
            '"03/01/2021");')
        self.c.execute(
            'INSERT INTO Products VALUES ("000004", "RacingCar", "Radio commanded racing car, boys favourite '
            'toy!", '
            '"16", "40", "03/01/2021");')
        self.c.execute('INSERT INTO Products VALUES ("000005", "Cluedo", "Classic murder mystery board game", "18", '
                       '"30", '
                       '"03/01/2021");')
        self.c.execute('INSERT INTO Products VALUES ("000006", "Army Man", "Classic miniature all-green army '
                       'soldier", "4.99", "50", "03/01/2021");')
        self.conn.commit()

    def fill_cat(self):
        self.c.execute('INSERT INTO Category VALUES ("0001", "Plush", "03/01/2021");')
        self.c.execute('INSERT INTO Category VALUES ("0002", "Doll", "03/01/2021");')
        self.c.execute('INSERT INTO Category VALUES ("0003", "RC", "03/01/2021");')
        self.c.execute('INSERT INTO Category VALUES ("0004", "BoardGame", "03/01/2021");')
        self.c.execute('INSERT INTO Category VALUES ("0005", "Blocks", "03/01/2021");')
        self.conn.commit()

    def fill_user(self):
        self.c.execute('INSERT INTO Users VALUES ("Gabriele", "1234", "ADMIN")')
        self.c.execute('INSERT INTO Users VALUES ("Diego", "0000", "User");')
        self.c.execute('INSERT INTO Users VALUES ("Rafael", "Password", "User");')
        self.conn.commit()

    def get_cred(self, event=0):
        user_input = self.username_entry.get()
        pass_input = self.password_entry.get()
        self.c.execute('SELECT * FROM Users WHERE Username = ? and Password = ?', (user_input, pass_input))
        char = self.cursor.fetchall()
        if (len(char) > 0):
            self.valid_login()
        else:
            self.non_valid_login()
        return

# def delete(self):


aat = DataBase("AllAToys.db")
# If no database remove comments
#aat.conn_cat()
#aat.conn_prod()
#aat.conn_user()
#aat.fill_prod()
#aat.fill_cat()
#aat.fill_user()





# connection.commit()
