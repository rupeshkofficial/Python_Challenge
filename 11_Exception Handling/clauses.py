try:
    my_list = [2,5,6,7,88,0]
    #print(my_list[76])                   # Invalid Index)
    #print(my_list[0] / my_list[-1])      # You cannot divide by zero 
    #my_list = my_list + "abc"             # Some error occured
    print(my_list[1])
except IndexError:
    print("Invalid Index")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some error occured")
else:
    print("Everything worked fine") # If no error in any parts then this else block will run.