stack = []

def pop():
    global stack
    if(len(stack)==0):
        return("error")
    else:
        ret = stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        return(ret)

def key(token, output):

    b = pop()
    if b=='error':
        return(True, "Missing token")
    elif token=='SHOW':
        output.append(("Output : ", b))
        return(False, "")

    a = pop()
    if a=='error':
        return(True, "Missing token")

    if token=='ADD':
        push(a + b)
    elif token=='SUB':
        push(a - b)
    elif token=='DIV':
        push(a / b)
    elif token=='MUL':
        push(a * b)

    return(False, "")


def push(num):
    stack.append(num)

def auto(lst, values, output):
    del stack[:]
    error = False
    errmsg = ""

    for tok in lst[::-1]:
        if tok[1]=='Variable':
            push(values[tok[0]])
        elif tok[1]=='Constant':
            push(tok[0])
        elif tok[1]=='Keyword':
            error, errmsg = key(tok[0], output);
        else:
            values[lst[0][0]] = pop()
            break;

    return output, values, error, errmsg
