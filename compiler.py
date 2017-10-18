from lexical import lex
from automata import auto

values = {}
f = open("code.txt", 'r')

for line in f:
    state_table = lex(line.strip())
    print(state_table)
    values = auto(state_table, values)
    print(values)

f.close()
