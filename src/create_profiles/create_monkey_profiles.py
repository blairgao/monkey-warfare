import os
import json
from dotenv import load_dotenv
from pathlib import Path

"""
Create a general profile for all monkeys from user input
"""

load_dotenv()
project_root = Path(os.getenv('PROJECT_ROOT',None))
if project_root is None:
    raise ValueError("PROJECT_ROOT not specified in .env file.")

fields = ["name", "number", "speed", "power", "defense"]
data = {}

#get the name of the colony first
invalid_input=True
while invalid_input:
    user_input = str(input(f"Enter the name of your monkey colony. Cannot leave blank: "))
    if len(user_input) > 0:
        invalid_input=False
data['name'] = user_input

for field in fields:
    if field == 'name':
        continue #already did name above
    invalid_input = True
    while invalid_input:
        user_input = input(f"Enter the monkey colony's {field} (int, 1-100): ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input >= 1 or user_input <= 100:
                invalid_input=False #break while loop
    data[field] = user_input

with open(os.path.join(project_root, "profiles", "monkey_colonies", f"monkey-{data['name']}.json"), 'w') as f:
    json.dump(data, f, indent=4)
