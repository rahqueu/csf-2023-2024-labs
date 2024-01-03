import json

with open('messages.json', 'r') as json_file:
    data = json.load(json_file)

with open('messages.txt', 'w') as output_file:
    for entry in data:
        author = entry['author']['username']
        content = entry['content']
        timestamp = entry['timestamp']
        
        output_file.write(f"{author} - \"{content}\" - \"{timestamp}\"\n")

print("Output file 'messages.txt' has been created.")

with open('messages.txt', 'r') as output_file:
    lines = output_file.readlines()

lines = lines[::-1]

with open('messages.txt', 'w') as output_file:
    output_file.writelines(lines)

