'''
Logical Operators are used to combine conditional statments. it's answer will always be TRUE or FALSE ( BOOLEAN VALUE)

AND ---> Returns TRUE if both the statments are true.               Ex: x < 10 and y < 15
OR  ---> Returns TRUE if one of the statments is true.              Ex: x < 15 or x < 24
NOT ---> Reverse the results, Returns FALSE if the result is true.  Ex: not(x < 15 and x < 120)

'''

physics = 67
chemistry = 19

print(physics > 33 and chemistry>33)
print(physics > 33 or chemistry>33)

print(not physics>33)
print(not (physics > 33 or chemistry > 33))