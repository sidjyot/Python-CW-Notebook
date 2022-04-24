try:
  f = open('input.txt')
except:
  print('File not found!')
#print(f)
else:  
  lines = f.readlines()
  
  for line in lines:
    try:
      numbers = line.split()
      first_number = int(numbers[0])
      second_number = int(numbers[1])
      print(f'Result: {first_number / second_number}')
    except ValueError:
      print('Something wrong with the inputs')
    except ZeroDivisionError:
      print('Cant divide by Zero!')
    except:
      print('Some bad happened! and i dont know what it is!')

      
  
  f.close()
