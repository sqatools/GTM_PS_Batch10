import json
import openpyxl

class Utils:
    def read_json_files(self, file_path):
        with open(file_path, "r") as file:
            file_data = file.read()
            json_data = json.loads(file_data)

        return json_data

    def read_excel_file(self, file_path, sheet_name, cell_name):
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name]
        cell = sheet[cell_name]
        return cell.value


if __name__ == '__main__':
    obj = Utils()
    # data = obj.read_json_files("sample_data.json")
    # print(data)
    # print(data['username'])
    data = obj.read_excel_file("test_data.xlsx", "Sheet1", "A1")
    print(data)