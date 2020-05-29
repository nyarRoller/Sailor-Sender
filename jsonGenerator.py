import json

base = {
    'questCount' : 1,
    
    'answers' : {
        '1': None,
        '2': None,
        '3': None,
        '4': None
    },

    'account':{
        'login' : None,
        'pasword' : None,

    },

    'enterInAccount' : False

}

with open("data.json", "r") as read_file:
    data = json.load(read_file)

    	
with open("data.json", "w") as write_file:
    json.dump(data, write_file, indent = 4)