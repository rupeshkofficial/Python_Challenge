# WITH keyword --> There is no need to write to f.close to close file. 
# Using with keyword if cursor move at the end of the file it will automatically close the file.

with open("/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/hello.txt", "r") as f:
    print(f.read())

print(f.read()) # ValueError: I/O operation on closed file. Because file has been read already and it is close. So, We can't do input output operation on closed file.