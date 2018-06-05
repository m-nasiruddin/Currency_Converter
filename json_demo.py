'''JavaScript Object Notation'''
import json


with open('input/states.json') as file:
    data = json.load(file)

for state in data['states']:
    print(state['name'], state['abbreviation'])

for state in data['states']:
    del state['area_codes']

with open('output/new_states.json', 'w') as file:
    json.dump(data, file, indent=2)
