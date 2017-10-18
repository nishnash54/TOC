stack = []

def pop():
    global stack
    if(len(stack)==0):
        return(-1)
    else:
        ret = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        return(ret)

def key(token):

    b = pop()
    if token=='SHOW':
        print("Output : ", b)
        return

    a = pop()
    if token=='ADD':
        push(a + b)
    elif token=='SUB':
        push(a - b)
    elif token=='DIV':
        push(a / b)
    elif token=='MUL':
        push(a * b)


def push(num):
    stack.append(num)

def auto(lst, values):
    del stack[:]

    for tok in lst[::-1]:
        if tok[1]=='Variable':
            push(values[tok[0]])
        elif tok[1]=='Constant':
            push(tok[0])
        elif tok[1]=='Keyword':
            key(tok[0]);
        else:
            values[lst[0][0]] = pop()
            break;

    return values
