import math

#s16099
#operator definitions
#a and b is swapped in some operations
#due to order they are being retrieved in
def operator_add(stack):#+
    a = stack.pop(); b = stack.pop()
    stack.append( a + b )
def operator_sub(stack):#-
    a = stack.pop(); b = stack.pop()
    stack.append( b - a)
def operator_mul(stack):#*
    a = stack.pop(); b = stack.pop()
    stack.append( a * b )
def operator_div(stack):#/
    a = stack.pop(); b = stack.pop()
    stack.append( b / a )
def operator_log(stack):#l
    a = stack.pop()
    stack.append(math.log(a))
def operator_pow(stack):#^
    a = stack.pop(); b = stack.pop()
    stack.append( b ** a )
def operator_sin(stack):#a
    a = stack.pop()
    stack.append(math.sin(a))
def operator_cos(stack):#b
    a = stack.pop()
    stack.append(math.cos(a))
def operator_tan(stack):#c
    a = stack.pop()
    stack.append(math.tan(a))
def operator_ctg(stack):#d
    a = stack.pop()
    stack.append(1 / math.tan(a))
def operator_sec(stack):#e
    a = stack.pop()
    stack.append(1 /  math.cos(a))
def operator_csc(stack):#f
    a = stack.pop()
    stack.append(1 / math.sin(a))
def operator_fac(stack):#!
    a = stack.pop()
    b = a#make a copy of a to reuse it as a loop limit
    i = 1
    while (i < b):
        a = i * a
        i += i 
    stack.append(a)

operators = {#assign operators to functions
    '+': operator_add,
    '-': operator_sub,
    '*': operator_mul,
    '/': operator_div,
    'l': operator_log,
    '^': operator_pow,
    'a': operator_sin,
    'b': operator_cos,
    'c': operator_tan,
    'd': operator_ctg,
    'e': operator_sec,
    'f': operator_csc,
    '!': operator_fac,
    }

def get_input(inp = None):#convert a string to a list       
    if inp is None:
        inp = input('expression: ')#get input from user
    tokens = inp.strip().split()
    return tokens

def calculate(tokens):
    stack = []
    for token in tokens:
        if token in operators:#f the token is an operator
            operators[token](stack)#match the token to an appropriate function
            print('perform operaton', repr(token), ' :', repr(stack))
        else:
            stack.append(int(token))#if the token is a number
            print('push ', repr(token), ' onto the stack: ', repr(stack))

def main():
    calculate(get_input())

if __name__ == "__main__":
    main()
