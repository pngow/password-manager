from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
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
        # set file_path to be the global variable
        global file_path

        output = store_password(file_path, website_input.get(), username_input.get(), password_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)

        if isinstance(output, int) and output == 1:
            result.config(text="Successfully added.")
        elif isinstance(output, int) and output == 2:
            result.config(text="File is not in CSV format.")
        elif isinstance(output, str) and os.path.isfile(output):
            result.config(text="File created & written to.")

            # update global file path variable to the new file
            file_path = output

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
        # set file_path to be the global variable
        global file_path

        password = query_password(file_path, website_input.get(), username_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)

        # output results
        if isinstance(password, int) and password == 1:
            # no file exists
            result.config(text="No password CSV file found.")
        elif isinstance(password, int) and password == 2:
            # file was not in csv format
            result.config(text='File not in CSV format.')
        elif isinstance(password, int) and password == 3:
            # no password matching the website & username
            result.config(text="No password found.")
        elif isinstance(password, str):
            # successfully retrieved password for the website & username
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
        # set file_path to be the global variable
        global file_path

        output = replace_password(file_path, website_input.get(), username_input.get(), password_input.get())

        # clear inputs in the entry fields
        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)

        if isinstance(output, int) and output == 1:
            # successfully updated password for the website & username
            result.config(text="Successfully updated.")
        elif isinstance(output, int) and output == 2:
            # file was not in csv format
            result.config(text="File is not in CSV format.")
        elif isinstance(output, int) and output == 3:
            # no file exists
            result.config(text="No password CSV file found.")
        elif isinstance(output, int) and output == 4:
            result.config(text='Error.')

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

# ask users to locate an existing password csv file
file_path = filedialog.askopenfilename(initialdir='/', title='Select CSV', filetypes=(('CSV files', '*.csv'), ('All files', '*.*')))
# format when no file selected
if file_path == "":
    file_path = None

# run gui
gui.mainloop()


