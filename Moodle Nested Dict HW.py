import json

with open('input.json') as input_json:
  json_data = json.load(input_json)

num_questions = 0
num_replies = 0
title_list = []
title_set = set()
user_list = []
user_set = set()
user_counter = {}

def myprint(input_str):
  print(json.dumps(input_str, indent = 4))

all_results = json_data['results']


# Sample access to one element 
#first_result = all_results[1]
#myprint(first_result)

for question in all_results:
  num_questions += 1
  all_replies = question['replies']
  course = question['course']
  title = course['title']
  title_list.append(title)
  
  for reply in all_replies:
    num_replies += 1
    user = reply['user']
    user_name = user['display_name']
    user_list.append(user_name)
    if user_name in user_counter:
      user_counter[user_name] += 1
    else:
      user_counter[user_name] = 1
    

print(f'Total number of Questions: {num_questions} and replies :  {num_replies}')

title_set = set(title_list)
print(f'Uniques titles are : {title_set}')

user_set = set(user_list)
print(f'Uniques users are : {user_set}')

print(f'\nThe users list as per number of replies is : ')
for k, v in sorted(user_counter.items(), key=lambda item: item[1], reverse = True):
    print(f'User : {k} \t Replies: {v}')