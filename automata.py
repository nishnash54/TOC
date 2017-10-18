stack = []

def pop():
    global stack
    if(len(stack)==0):
        return(-1)
    else:
        ret = stack[len(stack)-1]
        stack = stack[:len(stack)-2]
        return(ret)


def push(num):
    stack.append(num)

def auto(lst):

    print(stack)

    for i in lst:
        push(i)
    print(stack)

    for i in lst:
        pop()
    print(stack)
