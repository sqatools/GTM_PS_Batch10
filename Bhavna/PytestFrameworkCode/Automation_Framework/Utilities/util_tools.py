import json

class Utils:
    def read_json_files(self,file_path):
        with open(file_path,"r") as file:
            file_data = file.read()
            json_data = json.loads(file_data)

        return json_data


if __name__ == '__main__':
    obj = Utils()
    data = obj.read_json_files("sample_data.json")
    print(data)
    print(data['username'])