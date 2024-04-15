import json

def get_all_persons () :
    try :
        persons_data = ""
        with open ("./dataBase/db.json", "r") as db_file:
            persons_data = json.load(db_file)
            db_file.close()
        
        if len(persons_data) == 0:
            return 204

        return persons_data
    except :
        return 404
