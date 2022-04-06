import json

f = open('intents.json', 'r')
data = json.load(f)
print(data)

# with open('intents.json', 'r') as f:
#     intents = json.load(f)

# print(intents)