import json
def write_json(filepath,content):
    with open(filepath,"w") as f:
      data=json.dumps(content)
      f.write(data)

"""data1= {'Name':'Nagaratna','City':'Honnavar','Post':'gunavante'}     """
"""write_json("New_json.json",data1)  """

def read_json(filepath):
    with open(filepath,"r") as f2:
        data = f2.read()
        json_datas=json.loads(data)

    return json_datas
result= read_json('Dummy docs/New_json.json')
print(result)

result['City']= 'Mumbai'
result['Name'] = 'Misha'
write_json("Dummy docs/New_json.json", result)
data2= read_json('Dummy docs/New_json.json')
print(data2)