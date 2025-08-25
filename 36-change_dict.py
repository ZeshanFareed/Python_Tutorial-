# You can change the value of a specific item by referring to its key name:

# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)


# Update the "year" of the car by using the update() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"year": 2020})
print(car)