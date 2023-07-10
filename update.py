import os
import fileinput

def replace_password(file_path, website, username, new_password):
    try:
        # no file exists (3)
        if file_path is None or os.path.isfile(file_path):
            return 3
        # file not in csv format (2)
        elif file_path is not None and not file_path.lower().endswith('.csv'):
            return 2
        
        for line in fileinput.input(file_path, inplace=True):
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

        # successful update
        return 1
    except Exception as e:
        # no file exists (4)
        print(e)
        return 4