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
    new_error = False
    state_table = lex(line.strip())
    #print(state_table)
    output, values, new_error, errmsg = auto(state_table, values, output)
    #print(values)
    if new_error :
        error = True
        error_list.append((line_num, errmsg))

f.close()

if error:
    for each in error_list :
        print(each)
else :
    for each in output:
        print(each)
