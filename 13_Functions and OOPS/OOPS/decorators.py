# Decorator start with --> @

def make_pretty(fun): # Here ordinary fn passed
    def inner():
        print("I got decorated")
        fun()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()