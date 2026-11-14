
import re

# Step 1: Read the text file
with open("input.txt", "r") as file:
    text = file.read()

# Step 2: Create a regex pattern
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

# Step 3: Extract all email addresses
emails = re.findall(pattern, text)

# Step 4: Remove duplicate emails
unique_emails = set(emails)

# Step 5: Display the results
print("Extracted Email Addresses:")

if unique_emails:
    for email in sorted(unique_emails):
        print(email)
else:
    print("No email addresses found.")

# Step 6: Save emails into another file
with open("output.txt", "w") as file:
    for email in sorted(unique_emails):
        file.write(email + "\n")

print("\nEmails saved successfully in output.txt")
