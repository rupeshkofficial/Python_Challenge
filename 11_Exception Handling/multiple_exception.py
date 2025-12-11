# lst = [3,4,5,7,98,6,89,5]
# print(lst[1])
# print(lst[2])
# print(lst[65]) # IndexError: list index out of range
# print(lst[3])
# print(lst[7])

#print(10 / 0) # ZeroDivisionError: division by zero


# ----------------------- Multiple Exception Handling ----------

try:
    my_list = [2,5,6,7,88,0]
    #print(my_list[76])                   # Invalid Index)
    #print(my_list[0] / my_list[-1])      # You cannot divide by zero 
    my_list = my_list + "abc"             # Some error occured
except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some error occured")