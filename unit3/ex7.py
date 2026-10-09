import shutil
import os

with open("source.txt", "w") as f:
    f.write("Hello Python")

shutil.copy("source.txt", "copy.txt")
print("File copied")

shutil.move("copy.txt", "moved.txt")
print("File moved")

os.remove("moved.txt")
print("File deleted")
