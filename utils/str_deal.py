pre_str='a∧(e∧(¬b∧c∧d∨¬c∧b)∨¬(c∨d))∨¬a∧(c∧¬d∧e∨d∧¬e)'
print(len(pre_str))
for i in range(10):
    key='s['+str(i)+']'
    x=chr(ord('a')+i)
    pre_str=pre_str.replace(key,x)
    pre_str=pre_str.replace('¬'+x,chr(ord('A')+i))
pre_str=pre_str.replace('∧','&')
pre_str=pre_str.replace('∨','|')
pre_str=pre_str.replace('¬',' not ')
pre_str=pre_str.replace('→',' <= ')
pre_str=pre_str.replace('↔',' == ')
pre_str=pre_str.replace('⊕',' != ')
print(pre_str)