from tkinter import Tk, Entry, Button, Text, Label
from PySQLite_manager import SQLiteManager

manager = SQLiteManager()


def console_log(result):
    lbl_consolse.configure(text=result)


def db_connect(database):
    console_log(manager.db_connect(database))


def run_sql(sql):
    a = manager.any_sql(sql)
    console_log(a.description)


app = Tk()
app.geometry('1024x768')

e_database = Entry(app)
btn_connect = Button(app, text='connect', command=lambda: db_connect(e_database.get()))
t_sql = Text(app)
btn_run = Button(app, text='RUN', command=lambda: run_sql(t_sql.get("1.0", "end-1c")))
lbl_consolse = Label(app)

e_database.pack()
btn_connect.pack()
t_sql.pack()
btn_run.pack()
lbl_consolse.pack()

app.mainloop()
