# Remove duplicate emails from the list of emails.

emails = ['example1@gmail.com', 'example2@gmail.com', 'example1@gmail.com']
unique_emails = []
for email in emails:
    if not email in unique_emails:
        unique_emails.append(email)
print(unique_emails)