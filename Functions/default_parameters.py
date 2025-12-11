# --------- 2. Default Parameters
# If fn call with value and if the value not given then take by default 0 or anything mentioned their. As of now by deafult is 0

def total_marks(physics=0, maths=0, science=0, english=0, hindi=0):
    print(f"Your makrs in physics = {physics}")
    print(f"Your makrs in maths   = {maths}")
    print(f"Your makrs in science = {science}")
    print(f"Your makrs in english = {english}")
    print(f"Your makrs in hindi   = {hindi}")

    total = physics + maths + science + english + hindi
    print(f"Your total marks     = {total}")
total_marks(45,67) # Here Marks of Physics will be 45 and maths will be 67 and rest will be by deafult 0.
total_marks() # Marks of all subject will be by deafult 0
total_marks(maths=99,physics=44)


#------------------------------------------------------------------------------------
# Here: physics and maths marks is required parameters and science, english, hindi is default parameters.
# Required parameters will be in left side and default parametrs will be right side.

def total_marks(physics,maths, science=0, english=0, hindi=0): # Here to pass physics and maths marks is compulsory and rest if we not pass then by default will be 0
    print(f"Your makrs in physics = {physics}")
    print(f"Your makrs in maths   = {maths}")
    print(f"Your makrs in science = {science}")
    print(f"Your makrs in english = {english}")
    print(f"Your makrs in hindi   = {hindi}")

    total = physics + maths + science + english + hindi
    print(f"Your total marks     = {total}")

total_marks(maths=99,physics=44)
total_marks()