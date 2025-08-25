'''
JSON(Javascript Object Notation)
JSON text data ka format hota hy
it is mainly used for storing and transforming data b/w browser and server
zayada iska use api k case mein hoga

'''

import json

d = {
    "course_name" : "Python",
    "fees" : 12000
}

f = json.dumps(d)
print(f)
print(type(f))



print()
# convert json into python object or datatype
l = '[10, "xeeshan", 10.23]'

y = json.loads(l)
print(y)
print(type(y))


