import os
import sys

print("Current directory:", os.getcwd())

os.mkdir("TestFolder")
print("Directory created")

print("Files and folders:", os.listdir())

print("Python version:", sys.version)
print("Python platform:", sys.platform)

os.rmdir("TestFolder")
print("Directory removed")
