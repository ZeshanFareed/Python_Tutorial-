# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Xeeshan",
    "year" : 2005
  },
  "child2" : {
    "name" : "Imran",
    "year" : 2001
  },
  "child3" : {
    "name" : "Dani",
    "year" : 2003
  }
}
print(myfamily)


# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name" : "Xeeshan",
    "year" : 2005
  }
child2 = {
    "name" : "Imran",
    "year" : 2001
  }
child3 = {
    "name" : "Eisa",
    "year" : 2003
  }

new_dict = {
    "child_1" : child1,
    "child_2" : child2,
    "child_3" : child3
}
print(new_dict)



print()
# Access Items in Nested Dictionaries
# Print the name of child 2:
print(new_dict["child_2"]["name"])


print()
# Loop through the keys and values of all nested dictionaries:
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
