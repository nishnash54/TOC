keywords = {'ADD': '+',
            'SUB': '-',
            'DIV': '/',
            'MUL': '*',
            'SHOW': 'print'}

operators = {'<': '='}

def lex(line):

    tokens = line.split(' ')
    print("Tokens : ", tokens)

    token_list = []
    print("State table : ")
    for token in tokens:
        if token in keywords:
            print (token, "Keyword", keywords[token])
            token_list.append(keywords[token])
        elif token in operators:
            print (token, "Operator", operators[token])
            token_list.append(operators[token])
        else:
            print (token, "Variable")
            token_list.append(token)

    return token_list
