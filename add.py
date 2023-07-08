import constants
import os
import csv

def store_password(website, username, password):
    # create file and add header if it doesn't exist
    if not os.path.exists(constants.FILE_NAME):
        file = open(constants.FILE_NAME, "a+", newline='')

        # initialize csv writer
        writer = csv.writer(file, delimiter=',')

        writer.writerow(['website', 'username', 'password'])
    else:
        file = open(constants.FILE_NAME, "a+", newline='')

        # initialize csv writer
        writer = csv.writer(file, delimiter=',')

    # create entry
    entry = [website, username, password]

    # write to file
    writer.writerow(entry)

    file.close()

    return 1