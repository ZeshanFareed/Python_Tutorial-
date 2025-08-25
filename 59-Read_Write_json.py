import json

data = {
    "name": "Xeeshan",
    "age": 25,
    "city": "Lahore"
}

# Write JSON
file = open("data.json", "w")
file.write(json.dumps(data, indent=4))
file.close()

# Read JSON
file = open("data.json", "r")
content = file.read()
file.close()

finaldata = json.loads(content)
print("JSON Read Data : ", finaldata)
