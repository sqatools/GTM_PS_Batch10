# 02/07/2025 Session continue

import json

def read_json_content(filepath):
    with open(filepath,"r") as file:
        data = file.read()
        # convert json content to dictionary
        dict_data = json.loads(data)
    return dict_data

# data = read_json_content("userinfo.json")
# print(data)
# print("Name :",data['First_name'])
# print("Mobile No.", data['Mobile no.'])

def write_json_file(filepath,new_content):
    with open(filepath,"w") as file:
     # convert dictionary content to json
        json_data = json.dumps(new_content)
        print(json_data)
        file.write(json_data)

file_data = read_json_content("userinfo.json")
file_data['Address'] = 'Pune, Mahashtra'

write_json_file("userinfo.json",file_data)
