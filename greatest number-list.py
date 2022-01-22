#mylist = []
# for i in range(3):
#   print(f"enter a number at position {i + 1} : ", end="" )
#   temp = int(input())
# #  mylist.append(temp)
#print(f"Greatest number of these is", max(mylist))

a = int(input("Enter the first number please: "))
b = int(input("Enter the second number please: "))
c = int(input("Enter the third number please: "))

if a > b:
  if a > c:
    print(f'{a} is the greatest number in these numbers - a')
elif b > c:
  print(f'{b} is the greatest number in these numbers - b')
else:
  print(f'{c} is the greatest number in these numbers - c')

