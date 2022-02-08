import json

with open('input.json') as input_json:
  json_data = json.load(input_json)

#print(type(json_data))

def myprint(input_str):
  print(json.dumps(input_str, indent = 4))

all_results = json_data['results']
#print(type(all_results))
#myprint(json_data)

# Sample access to one element 
first_result = all_results[1]
myprint(first_result)

