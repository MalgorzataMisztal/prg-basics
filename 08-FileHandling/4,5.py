import re

file_name = 'email.txt'

with open(file_name, 'r', encoding='utf-8') as file:
    content = file.read()

def email_sender(content):
    match1 = re.search(r'From: .* <(.*)>', content)
    if match1:
        return match1.group(1)

def email_recipient(content):
    match2 = re.search(r'To: .* <(.*)>', content)
    if match2:
        return match2.group(1)

def email_subject(content):
    match3 = re.search(r'Subject: (.*)', content)
    if match3:
        return match3.group(1)

def email_body(content):
    match4 = re.search(r'\n\n(.*)', content, re.DOTALL)
    if match4:
        return match4.group(1).strip()
    
print("Sender:",    email_sender(content))
print("Recipient:", email_recipient(content))
print("Subject:",   email_subject(content))
print("\nBody:\n",  email_body(content))