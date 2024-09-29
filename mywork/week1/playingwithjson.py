# playing with json
# Author: Andre Hoarau
import json
data ={
    'name': 'joe',
    'age': 21,
    "student": True
}
jsonString = json.dumps(data)
print (data)
print(jsonString)