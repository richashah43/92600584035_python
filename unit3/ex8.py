import re

text = "My phone number is 9876543210"

pattern = r"\d{10}"

result = re.findall(pattern, text)

print("Phone number:", result)
