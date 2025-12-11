with open("/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/hello.txt", "r") as f:

    print(f) # <_io.TextIOWrapper name='/Users/rupeshk/Desktop/Coding/Python_Challenge/12_File Handling/hello.txt' mode='r' encoding='UTF-8'>

    for line in f:
        print(line, end = " ") # Ye ek ek line file ka print krega



    # x = f.read() # Jitne sare file ke text hai o ab x me aa jayenge. Then x hamra ab string ban gya aur hm string ke upar iterate kr sakte hai aur uske ek ek character print kr sakte hai.
    # print(x)
    # for ch in x:
    #     print(ch)
    
    