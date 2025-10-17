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

3. Division ( % ) --> Output always in float ---> Ex: 10 % 4 = 2.5, 10 % 10 = 1.0

4. Floor Division ( // ) --> Output always in integer ( That is always gives lower integer) 
                       
                         Ex: 10 % 4 = 2.5 but we do 10 // 4 (floor division) then we have to take lower integer then it's output will be 2.
                            13 % 7 = 1.8571 but we do 13 // 7 (floor division) then we have to take lower integer then it's output will be 1.
                             
                                        

''' 

a = 40
b = 4

print(a+b)
print(a-b)
print(a/b) 
print(a*b)

print(a**b)
print(a%b) # % ---> Gives remainder

print(a//b) # // --> Floor divison (Return always integer)
