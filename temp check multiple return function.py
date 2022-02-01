### Write your function here
def check_temp(temperature):
  if temperature > 29:
    return 'Too hot!'
  elif temperature < 21:
    return 'Too cold!'
  else:
    return 'OK'
###


if __name__ == '__main__':
  print(check_temp(24))
  print(check_temp(10))

  # Add more testing here.
  print(check_temp(21))
  print(check_temp(29))
  print(check_temp(201))
  print(check_temp(1))
  
        