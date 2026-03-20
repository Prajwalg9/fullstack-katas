"""
Ravi Kumar, Email: ravi.kumar123@example.com, Phone: +91-98765-43210
Seema Sharma, Email: seema_sharma@example.org, Phone: 022-23456789
Invalid line, Email: test@@example, Phone: 12345
Support, Email: support@my-site.co.in, Phone: +1-202-555-0187
"""
import re

with open("raw Emails.php", "rt", encoding="utf-8", errors="replace") as f:
    data = f.read()

# Step 1: strip Markdown link wrapper: [text](mailto:text)
# This replaces "[something](mailto:something)" with just "something"
data = re.sub(r'\[([^\]]+)\]\(mailto:[^)]+\)', r'\1', data)

# Step 2: extract emails
# Explanation:
#   ^ not used here because we scan whole text
#   [\w\.-]+  -> local part (letters, digits, underscore, dot, hyphen)
#   @
#   [\w\.-]+  -> domain and subdomain
#   \.
#   [a-zA-Z]{2,} -> TLD (2+ letters: com, org, co.in -> "in" is last part)
pattern = r'\b[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}\b'

emails = re.findall(pattern, data)

for email in emails:
    print(email)
