import re

class Reader:
    "This is Amy and Martin's Lisp Reader"
    def __init__(self, tokens):
        self.position = 0
        self.tokens   = tokens
    def next(self):
        self.position = self.position + 1
        return self.tokens[self.position - 1]
    def peek(self):
        return self.tokens[self.position]

def read_str(s):
    tokens = tokenizer(s)
    reader = Reader(tokens)
    return read_form(reader)

def tokenizer(s):
    ptn = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"|;.*|[^\s\[\]{}('"`,;)]*)""")
    return re.findall(ptn, s)

def read_form(rdr):
    char = rdr.peek()
    if char == "(":
        return read_list(rdr)
    else:
        return read_atom(rdr)

def read_list(rdr):
    xs = []
    while rdr.next() != ")":
        xs.append(read_form(rdr))
    return xs

class Symbol(str):
    pass

def _symbol_Q(exp):
    return type(exp) == Symbol

def read_atom(rdr):
    int_ptn = re.compile("\d+")
    float_ptn = re.compile("\d+\.\d+")
    tkn = rdr.peek()

    if re.match(int_ptn, tkn):
        return int(tkn)
    elif re.match(float_ptn, tkn):
        return float(tkn)
    else:
        return Symbol(tkn)


r = Reader([1, 2, 3])
