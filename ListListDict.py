# Anonymous dict for List of Lists containg Dicts
import json

family1 = [
  {
    'name' : 'Sidharth',
    'age' : 47,
    'profession' : 'Papa Coder'
  },
  {
    'name' : 'Nikunj',
    'age' : 10,
    'profession': 'Budding Coder'
  },
  {
    'name' : 'Mandar',
    'age' : 16,
    'profession': 'Fiery Teen'
  }
]


family2 = [
  {
    'name' : 'Mahesh',
    'age' : 45,
    'profession' : 'Another Papa'
  },
  {
    'name' : 'Ramesh',
    'age' : 15,
    'profession': 'Pro Coder'
  }
]


family3 = [
  {
    'name' : 'Suresh',
    'age' : 54,
    'profession' : 'Oldest Papa'
  },
  {
    'name' : 'Mohan',
    'age' : 25,
    'profession': 'Expert Coder'
  }
]

coder_families = [family1, family2, family3]
print(json.dumps(coder_families, indent=4))