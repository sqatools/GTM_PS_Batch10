import json


def read_json_content(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        dict_data = json.loads(data)
        return dict_data


data = read_json_content("userinfo_data.json")
print(data)
# {'first_name': 'Rahul', 'last_name': 'Gupta', 'Age': 35, 'email': 'rahul@gmail.com', 'phone': 6554645645, 'Address': 'Mumbai , Boriwali'}

print("Name :", data['first_name'])
# Name : Rahul

print("Email :", data['email'])
# Email : rahul@gmail.com

print("Name :", read_json_content("userinfo_data.json")['first_name'])
# Name : Rahul


def write_json_file(filepath, new_content):
    with open(filepath, "w") as file:
        json_data = json.dumps(new_content)
        print(json_data)
        file.write(json_data)


file_data = read_json_content("userinfo_data.json")
file_data['Address'] = 'Mumbai , Boriwali'

write_json_file("userinfo_data.json", file_data)
