# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
firms = OrderedDict(json.loads(input()))

# your code here
firms.popitem()
firms.popitem()

# Print the altered version
print(firms)