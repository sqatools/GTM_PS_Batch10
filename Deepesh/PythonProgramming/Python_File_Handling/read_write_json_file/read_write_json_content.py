import json
def read_json_content(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        # convert json content to dictionary
        dict_data = json.loads(data)
    return dict_data


# data = read_json_content("userinfo_data.json")
# print(data)
# print("Name :", data['first_name'])
# print("Email :", data['email'])
#
#
# print("Name:", read_json_content("userinfo_data.json")['first_name'])


def write_json_file(filepath, new_content):
    with open(filepath, "w") as file:
        # # convert dictionary content to json
        json_data = json.dumps(new_content)
        print(json_data)
        file.write(json_data)


file_data = read_json_content("userinfo_data.json")
file_data['Address'] = 'Mumbai , Boriwali'

write_json_file("userinfo_data.json", file_data)
