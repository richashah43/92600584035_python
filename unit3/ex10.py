import re

with open("details.txt", "r") as f:
    text = f.read()

name = re.search(r"Name:\s*(.*)", text).group(1)
age = re.search(r"Age:\s*(\d+)", text).group(1)
email = re.search(r"Email:\s*(\S+)", text).group(1)
phone = re.search(r"Phone:\s*(\d+)", text).group(1)

print("Name:", name)
print("Age:", age)
print("Email:", email)
print("Phone:", phone)
