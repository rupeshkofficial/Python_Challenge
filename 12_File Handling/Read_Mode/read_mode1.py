# Read Mode --> To read content of the file

f = open("/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/Read_Mode/hello.txt", "r") # With Proper path of file
#f = open("hello.txt","r") # If file is in same folder then no need to give path. Just give file name

# x = f.read() # It will read all the content of file and save it to x
# print(x)


#print(f.read(5)) # It will read only 1st 5 charcter of the file
#print(f.read(5)) # It will read next 5 charcter of the file ( Internally curser move from the first 5 charcter so when we read again then it will read 5 character from 6th character)

#print(f.readline()) # It will read one line only
#print(f.readline())

print(f.readlines()) # It will read all line one by one
f.close()