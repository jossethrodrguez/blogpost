from pathlib import Path
import json

username = input("What is your name? ")
contents = json.dumps(username)
path = Path('username.json')
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")

read_contents = path.read_text()
username = json.loads(read_contents)
print(f"Welcome back, {username}!")
