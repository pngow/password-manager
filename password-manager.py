from tkinter import *
from tkinter.ttk import *
from functools import partial
from add import store_password
# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

def add_password():
    # Toplevel object as new window
    add_window = Toplevel(gui)

    # set size of window
    add_window.geometry("200x200")

    # heading
    Label(add_window, text="Add Password").pack()

    # website name
    Label(add_window, text="Website").pack()
    website_input = Entry(add_window)
    website_input.pack()

    # username
    Label(add_window, text="Username").pack()
    username_input = Entry(add_window)
    username_input.pack()

    # password
    Label(add_window, text="Password").pack()
    password_input = Entry(add_window)
    password_input.pack()

    # inner function to send data to be stored in the csv
    def submit_add():
        store_password(website_input.get(), username_input.get(), password_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)

    # submit button
    Button(add_window, text="Submit", command=submit_add).pack()


gui = Tk()
# set size of window
gui.geometry("200x200")
# set title of window
gui.title("Password Manager")

Label(gui, text="Password Manager").pack()

# add password feature
Button(gui, text="Add Password", width= 25, command=add_password).pack()

# query password feature
Button(gui, text="Search For A Password", width=25).pack()

# update a password
Button(gui, text="Update A Password", width=25).pack()

# run gui
gui.mainloop()


