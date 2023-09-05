import json

json_string = input()

python_obj = json.loads(json_string)

print(type(python_obj))
print(python_obj)
