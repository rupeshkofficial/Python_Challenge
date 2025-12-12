import os

if os.path.exists("hello.txt"):
    os.remove("hello.txt")
    print("File deleted")
else:
    print("File does not exist")