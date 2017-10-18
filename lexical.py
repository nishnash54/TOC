keywords = {'ADD': '+',
            'SUB': '-',
            'DIV': '/',
            'MUL': '*',
            'SHOW': 'print'}

operators = {'<': '='}

def lex(line):

    tokens = line.split(' ')

    state_table = []
    for token in tokens:
        if token in keywords:
            state_table.append((token, "Keyword", keywords[token]))
        elif token in operators:
            state_table.append((token, "Operator", operators[token]))
        else:
            if token.isdigit():
                state_table.append((float(token), "Constant"))
            else:
                state_table.append((token, "Variable"))

    return state_table
