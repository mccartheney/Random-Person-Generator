# import json to get data from file
import json

# funtio to get all persons
def get_all_persons () :
    try :
        # initialize persons data
        persons_data = ""

        # open databse file
        with open ("./dataBase/db.json", "r") as db_file:
            # load json from database
            persons_data = json.load(db_file)

            # close database
            db_file.close()
        
        # if database is empty
        if len(persons_data) == 0:
            return 204

        # return data
        return persons_data
    except :
        # if data base dont exists
        return 404
