'''
                          Split and Join


a = "Hello world this is python"

words = a.split() ---> It is by default splitted by spaces

O/P: ["Hello", "world", "this", "is", "python"]

 ----> To split by hyphen : a.split("_")


'''

a1 = "Hello world this is python"
words1 = a1.split()
print(words1) # ['Hello', 'world', 'this', 'is', 'python']


a2 = "Hello_world_this_is_python"
words2 = a2.split()
words3 = a2.split("_")
print(words2) # ['Hello_world_this_is_python']
print(words3) # ['Hello', 'world', 'this', 'is', 'python']
print(len(words3)) # 5