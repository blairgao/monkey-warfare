import os
import json
from dotenv import load_dotenv
from pathlib import Path

"""
Create a user profile that will fight the monkeys
"""

load_dotenv()
project_root = Path(os.getenv('PROJECT_ROOT',None))
if project_root is None:
    raise ValueError("PROJECT_ROOT not specified in .env file.")

fields = ["name", "number", "speed", "power", "defense"]
data = {}

#get the users name first
invalid_input=True
while invalid_input:
    user_input = str(input(f"Enter your name. Cannot leave blank: "))
    if len(user_input) > 0:
        invalid_input=False
data['name'] = user_input

for field in fields:
    if field == 'name':
        continue #already did name above
    invalid_input = True
    while invalid_input:
        user_input = input(f"Enter your {field} (int, 1-100): ")
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input >= 1 or user_input <= 100:
                invalid_input=False #break while loop
    data[field] = user_input

with open(os.path.join(project_root, "profiles", "users", f"user-{data['name']}.json"), 'w') as f:
    json.dump(data, f, indent=4)
