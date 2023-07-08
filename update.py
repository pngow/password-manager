import constants
import fileinput

def replace_password(website, username, new_password):
    for line in fileinput.input(constants.FILE_NAME, inplace=True):
        split_line = line.split(sep=',')

        # line contains the website and username for the new password
        if split_line[0] == website and split_line[1] == username:
            # create new entry
            new_entry = ','.join([website, username, new_password])
            # write new entry to the csv file
            print(new_entry)
        else:
            # write original line back to the csv file
            print(line, end='')

    return 1