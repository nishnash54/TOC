from lexical import lex
from automata import auto

values = {}
f = open("code.txt", 'r')

line_num = 0
error_list = []
error = False
errmsg = ""
output = []

for line in f:
    line_num += 1
    state_table = lex(line.strip())
    #print(state_table)
    output, values, error, errmsg = auto(state_table, values, output)
    #print(values)
    if error :
        print(line_num, errmsg)
        break
    else:
        if output:
            print(output)
        del output[:]

f.close()
