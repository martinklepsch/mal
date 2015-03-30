def READ (s):
    return s

def EVAL (s):
    return s

def PRINT (s):
    return s

def rep (s):
    return PRINT(EVAL(READ(s)))

while True:
    try:
        n = raw_input("user> ")
        print(rep(n))
    except EOFError:
        print "^D"
        exit()
