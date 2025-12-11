# Write and Append Mode in Python
'''
1. Can't read the file if we open the file in write mode. we will get error like this io.UnsupportedOperation: not readable. if we try to read file in write mode.
2. Write mode override the previous text. 
3. 
'''

with open("/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/Write_Mode/hello.txt", "w") as f:
    f.write("Good Bye!\n")
    f.write("Kaise bhai\n")
    f.write("mst bro hai bhai\n")
    f.write("kem cho!!")

#In read mode, if we give any file name that doesn't exist then it will throw error. But in write mode it doesn't throw error anbd it will create that file name by default.
with open("/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/Write_Mode/hello1.txt", "w") as f:
    f.write("Goo3ed Bye!\n")
    f.write("Kaise bhe23ai\n")
    f.write("mst bro2e hai bhai\n")
    f.write("kem cho2!!")