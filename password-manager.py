from tkinter import *
from tkinter.ttk import *
from add import store_password
from search import query_password
from update import replace_password
# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter

# NOTE ask users where their password csv is located?
# https://coderslegacy.com/python/libraries-in-python/python-tkinter-filedialog/

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
        output = store_password(website_input.get(), username_input.get(), password_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)

        if output == 1:
            result.config(text="Successfully added.")

    # submit button
    Button(add_window, text="Submit", command=submit_add).pack()

    result = Label(add_window, text="")
    result.pack()

def search_password():
    # Toplevel object as new window
    search_window = Toplevel(gui)

    # set size of window
    search_window.geometry("200x200")

    # heading
    Label(search_window, text="Search Password").pack()

    # website name
    Label(search_window, text="Website").pack()
    website_input = Entry(search_window)
    website_input.pack()

    # username
    Label(search_window, text="Username").pack()
    username_input = Entry(search_window)
    username_input.pack()

    # inner function to send data to be search in the csv
    def submit_search():
        password = query_password(website_input.get(), username_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)

        # output results
        if isinstance(password, int) and password == 1:
            result.config(text="No password CSV file found.")
        elif isinstance(password, int) and password == 2:
            result.config(text="No password found.")
        else:
            result.config(text=password)

    # submit button
    Button(search_window, text="Submit", command=submit_search).pack()

    result = Label(search_window, text="")
    result.pack()

def update_password():
# Toplevel object as new window
    update_window = Toplevel(gui)

    # set size of window
    update_window.geometry("200x200")

    # heading
    Label(update_window, text="Update Password").pack()

    # website name
    Label(update_window, text="Website").pack()
    website_input = Entry(update_window)
    website_input.pack()

    # username
    Label(update_window, text="Username").pack()
    username_input = Entry(update_window)
    username_input.pack()

    # password
    Label(update_window, text="Password").pack()
    password_input = Entry(update_window)
    password_input.pack()

    # inner function to send data to be stored in the csv
    def submit_add():
        output = replace_password(website_input.get(), username_input.get(), password_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)

        if output == 1:
            result.config(text="Successfully updated.")

    # submit button
    Button(update_window, text="Submit", command=submit_add).pack()

    result = Label(update_window, text="")
    result.pack()

gui = Tk()
# set size of window
gui.geometry("200x200")
# set title of window
gui.title("Password Manager")

Label(gui, text="Password Manager").pack()

# add password feature
Button(gui, text="Add Password", width= 25, command=add_password).pack()

# query password feature
Button(gui, text="Search For A Password", width=25, command=search_password).pack()

# update a password
Button(gui, text="Update A Password", width=25, command=update_password).pack()

# run gui
gui.mainloop()


