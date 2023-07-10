import csv

def query_password(file_path, website, username):
    try:
        # file not in csv format (2)
        if file_path is not None and not file_path.lower().endswith('.csv'):
            return 2

        with open(file_path, 'r') as file:
            extracted = csv.reader(file, delimiter=',')

            # initialize search result as none
            result = None

            for entry in extracted:
                # website name and username match user input
                if entry[0] == website and entry[1] == username:
                    # retrieve password
                    result = entry[2]
                    break

            # no password found (3)
            if result is None:
                result = 3
            
            return result
    except Exception as e:
        # no file exists (1)
        print(e)
        return 1