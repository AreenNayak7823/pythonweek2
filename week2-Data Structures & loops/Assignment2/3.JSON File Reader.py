import json

filename = input("Enter JSON file name: ")

with open(filename, 'r') as file:
    data = json.load(file)

print("Formatted JSON Output:")
print(json.dumps(data, indent=4))
