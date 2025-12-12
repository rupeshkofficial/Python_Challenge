# ----------- 1. Named Parameters/Arguments


def total_marks(physics, maths, science, english, hindi):
    total = physics + maths + science + english + hindi
    print(total)


total_marks(56, 98, 79, 32, 83)
total_marks(science=98, hindi=43, maths=89, physics=94, english=73)  # Named Parameters
total_marks(56,98, hindi=43, english=23, science=98) # Named wala parametrs always will be in right side not in left side and normal will be in left side
