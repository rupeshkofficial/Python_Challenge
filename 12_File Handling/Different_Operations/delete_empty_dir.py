import os

# Deleting an empty directory/folder

if os.path.exists("Folder1"):
    os.rmdir("Folder1")
    print("Directory deleted.")
else:
    print("Directory does not exist")
