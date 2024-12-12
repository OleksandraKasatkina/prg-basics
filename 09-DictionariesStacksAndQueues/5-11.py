import json

# File to store voting data
voting_file = "voting.json"

# Load existing voting data from the JSON file
try:
    with open(voting_file, "r") as file:
        voting_data = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty dictionary
    voting_data = {}

# Prompt user for the person they want to vote for
person_name = input("Name of the person you are voting for: ").strip()

# Update the voting data
if person_name in voting_data:
    voting_data[person_name] += 1
else:
    voting_data[person_name] = 1

# Save the updated voting data back to the JSON file
with open(voting_file, "w") as file:
    json.dump(voting_data, file, indent=4)

print(f"Vote recorded for {person_name}!")
