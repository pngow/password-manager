import constants
import os

def store_password(website, username, password):
    # create file and add header if it doesn't exist
    if not os.path.exists(constants.FILE_NAME):
        file = open(constants.FILE_NAME, "a+")
        file.write('website,username,password')
    else:
        file = open(constants.FILE_NAME, "a+")

    # create entry
    entry = f"\n{website},{username},{password}"

    # write to file
    file.write(entry)

    file.close()
