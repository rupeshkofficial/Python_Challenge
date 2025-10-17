# Operators ---> To perform operations on varibales and values

'''
Different Types of Operators:-

1. Arithmetic Operators --> To perform mathematical operations ( +, -, %, /, **, //)
2. Assignment Operators  ---> =
3. Comparison Operators 
4. Logical Operators 

5. Identity Operators 
6. Membership Operators 
7. Bitwise Operators

Note:

1. Modulus ( % ) --> Gives remainder --> Ex: 10 % 3 = 1 , 5% 3 = 2, 
                                         5 % 10 =  5 ( Jab left wali value choti hoti hai right wali value se to remainder left wali value hoti hai)
                                         9 % 10 = 9
                                         10 % 10 = 0

2. Exponential ( ** ) --> Power --> Ex: 5**3 = 125

3. Division ( / ) --> Output always in float ---> Ex: 10 / 4 = 2.5, 10 / 10 = 1.0

4. Floor Division ( // ) --> Output always in integer ( That is always gives lower integer) 
                       
                         Ex: 10 / 4 = 2.5 but when we do 10 // 4 (floor division) then we have to take lower integer (Never do roundoff) then it's output will be 2.
                             13 / 7 = 1.8571 but when we do 13 // 7 (floor division) then we have to take lower integer (Never do roundoff) then it's output will be 1.
                             - 10 / 4 = -2.5 but but when we do -10 // 4 (floor division) then we have to take lower integer (Never do roundoff) then it's output will be -3.
                                         As lower integer of -2.5 will be -3.


''' 

a = 40
b = 4

print(a+b) # 44
print(a-b) # 40
print(a/b) # 10.0 ( Always Float)
print(a*b) # 160

print(a**b) # 2560000
print(a%b) # 0 ( Gives Remainder)

print(a//b) # 10 ( Floor Division always return integer value)
