# Lambda ---> Anonymous function

# ----------->>  Normal Fn
def add_numbers(n1,n2,n3):
    return n1 + n2 + n3

print(add_numbers(10,20,30)) # 60



# ----------->>  Lambda Fn  Just in one line code
# Example 1
add_numbers = lambda n1,n2,n3 : n1 + n2 + n3  # Here Lambda fn will take 3 arguments n1,n2,n3 and add them and then return their addition
print(add_numbers(10,20,30)) # 60