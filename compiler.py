from lexical import lex
from automata import auto

f = open("code.txt", 'r')

for line in f:
    token_lst = lex(line.strip())
    print(auto(token_lst))

f.close()
