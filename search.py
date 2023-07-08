import constants
import csv

def query_password(website, username):
    try:
        with open(constants.FILE_NAME, 'r') as file:
            extracted = csv.reader(file, delimiter=',')

            # initialize search result as none
            result = None

            for entry in extracted:
                # website name and username match user input
                if entry[0] == website and entry[1] == username:
                    # retrieve password
                    result = entry[2]
                    break

            # no password found (2)
            if result is None:
                result = 2
            
            return result
    except Exception as e:
        # no file exists (1)
        print(e)
        return 1