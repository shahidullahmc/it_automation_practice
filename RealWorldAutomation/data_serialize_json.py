import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)
    