import json

with open('city.txt', 'r',encoding='utf-8') as file:
    file_content = file.read()

data_list = file_content.split(', ')
data_dict = {}
for item in data_list:
    key, value = item.split(':')
    data_dict[key.strip()] = value.strip()
json_data = json.dumps(data_dict, indent=4)

print(json_data)























