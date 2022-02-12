#date examples
from datetime import date

f_date = date(2022, 2, 16)
l_date = date(2022, 3, 12)
delta = l_date - f_date
#print(delta.days)
print(f'Overdue amount : {round((delta.days * 0.15), 2)}')
