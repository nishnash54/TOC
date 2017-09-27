keywords = {'ADD': '+',
            'SUB': '-',
            'DIV': '/',
            'MUL': '*',
            'SHOW': 'print'}

operators = {'<': '='}

line = raw_input('Enter line of code : ').strip()
tokens = line.split(' ')
print("Tokens : ", tokens)

print("State table : ")
for token in tokens:
    if token in keywords:
        print (token, "Keyword", keywords[token])
    elif token in operators:
        print (token, "Operator", operators[token])
    else:
        print (token, "Variable")
