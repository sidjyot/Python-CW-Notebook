import json

with open('input.json') as input_json:
  json_data = json.load(input_json)

#print(json_data)
print(type(json_data))

all_results = json_data['results']
print(type(all_results))

first_result = all_result[1]

print
