import reader, printer

def READ (s):
    return reader.read_str(s)

def EVAL (s):
    return s

def PRINT (data):
    return printer.pr_str(data)

def rep (s):
    return PRINT(EVAL(READ(s)))

while True:
    try:
        n = raw_input("user> ")
        print(rep(n))
    except EOFError:
        print "^D"
        exit()
