import json

f = open('data.json')
data = json.load(f)
for i in data['empDetails']:
    print(i)

f.close()
