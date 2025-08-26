import json

class Utils:
    def read_json_file(self, file_path):
        with open(file_path, "r") as file:
            file_data = file.read()
            json_data = json.loads(file_data)

        return json_data


if __name__ == '__main__':
    obj = Utils()
    data = obj.read_json_file("sample_data.json")
    print(data)
    print(data['username'])