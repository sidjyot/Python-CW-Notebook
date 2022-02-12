#Method 1 - named dict 

sid = {
  'name': 'Sidharth'
}

nik = {
  'name': 'Nikunj'
}

family = [sid, nik]

for member in family: 
  print(member)

#Method 2 - anonymous dict

family1 = [
  {
    'name' : 'Sidharth'
  },
  {
    'name' : 'Nikunj'
  }
]


for member in family1: 
  print(member)