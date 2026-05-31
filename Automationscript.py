import re

# Open text file
file = open("sample.txt/sample.txt", "r")
data = file.read()

# Find emails
emails = re.findall(r'\S+@\S+', data)

# Save emails to another file
output = open("emails.txt", "w")

for email in emails:
    output.write(email + "\n")

output.close()

print("Emails extracted successfully!")