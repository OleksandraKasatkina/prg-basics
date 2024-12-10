import emails

# Read the email content from the file
email_file = "email.txt"
with open(email_file, "r", encoding="utf-8") as file:
    email_content = file.read()

# Extract and print the details
sender = emails.email_sender(email_content)
recipient = emails.email_recipient(email_content)
subject = emails.email_subject(email_content)
body = emails.email_body(email_content)

print(f"Sender Email: {sender}")
print(f"Recipient Email: {recipient}")
print(f"Subject: {subject}")
print("Body: ")
print(body)
