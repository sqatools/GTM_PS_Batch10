"""✅ json.load() reads JSON and converts it to a Python dictionary.

✅ json.dumps() converts a Python dictionary to a JSON string."""

import json

def write_json(filepath,content):
    with open(filepath,"w") as f:
        data=json.dumps(content)
        f.write(data)

#data={'name':'vaishnavi','Age':29,'Occupation':'Software Engg','city':'Bangalore'}
#write_json("New_Jsonfile.json",data)

def read_json(filepath):
    with open(filepath,"r") as f1:
        data=f1.read()
        json_data=json.loads(data)
    return json_data

data1=read_json("New_Jsonfile.json")
print(data1)
data1['city']='Bangalore,Bagalkot'
data1['Address']='BTM Layout'
data1['Qualification']='B.E , MBA'
write_json("New_Jsonfile.json",data1)

