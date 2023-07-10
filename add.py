import os
import csv

# default file name
file_name = "password_master.csv"

def store_password(file_path, website, username, password):
    # reference the global file_name variable
    global file_name

    # flag to determine whether a new file was created
    new_file = False

    # create file and add header if it doesn't exist
    if file_path is None or os.path.isfile(file_path):
        # add suffix to default file name if already exists in file system
        suffix = 1
        while os.path.isfile(file_name):
            file_name = "password_master_" + str(suffix) + '.csv'
            suffix += 1

        file = open(file_name, "a+", newline='')

        # set new file flag to True
        new_file = True

        # initialize csv writer
        writer = csv.writer(file, delimiter=',')

        writer.writerow(['website', 'username', 'password'])
    elif file_path is not None and file_path.lower().endswith('.csv'):
        file = open(file_path, "a+", newline='')

        # initialize csv writer
        writer = csv.writer(file, delimiter=',')
    else:
        # file is not in csv format
        return 2

    # create entry
    entry = [website, username, password]

    # write to file
    writer.writerow(entry)

    file.close()

    if new_file:
        # return path of csv file
        return os.getcwd() + '\\' + file_name
    else:
        return 1