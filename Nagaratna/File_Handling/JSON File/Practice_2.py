import json
def write_json(filepath,content):
    with open(filepath,"w") as f:
      data=json.dumps(content)
      f.write(data)
      print(data)

write_json("Dummy docs/New_json.json", "Hello python")

def read_json2(filepath,content):
    with open(filepath,"w") as file:
        data1= json.dumps(content)
        file.write(data1)
    print(data1)

read_json2("Write_new file","Adding new content to the file ")

