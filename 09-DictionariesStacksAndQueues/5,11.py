import json
file_name = 'voting.json'

try:
    with open(file_name, 'r', encoding ='utf-8') as file:
        votes = json.load(file)
except FileNotFoundError:
    votes = {}

person_name = input('Name of the person you are voting for:')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open(file_name, 'w', encoding = 'utf-8') as file:
    json.dump(votes, file, indent=3)

print(f"Vote recorded. Current status: {votes}")