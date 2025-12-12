import shutil
import os

# Deleting a directory and it's content

if os.path.exists("Folder2"):
    shutil.rmtree("Folder2")
    print("Directory and its content deleted.")
else:
    print("Directory does not exist.")
