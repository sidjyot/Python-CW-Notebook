#Dicts
myCar = {
  "model": "i10",
  "year": 2013,
  "color": "Grey"
}

# Printing a dictionary
print(myCar)

# Access Items
print(myCar["year"])
print(myCar.get("model"))

# Change Items
myCar["model"] = "Mercedes"
myCar.update({"year": 2022})
print(myCar)

# Add Items
myCar["topSpeed"] = 350
print(myCar)

# Remove Items
myCar.pop("topSpeed")
print(myCar)

# Looping thru a dict
for i in myCar:
  print(i, ":", myCar[i])

# Copy dictionary
myWifesCar = myCar.copy()
print(myWifesCar)

mySonsCar = dict(myWifesCar)
print(mySonsCar)

# Clear dictionary
myCar.clear()
print(myCar) 

#delete
del myCar
print(myCar)