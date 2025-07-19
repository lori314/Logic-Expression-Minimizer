def prove(shi,value_list):
    flag=1
    for value in value_list:
        a=value[0]
        b=value[1]
        c=value[2]
        d=value[3]
        e=value[4]
        A=a^1
        B=b^1
        C=c^1
        D=d^1
        E=e^1
        if not eval(shi)==value[5]:
            flag=0
            print(value)
    if flag==0:
        return  False
    elif flag==1:
        return True

value_list=[]
count=0
data_str='''0	0	0	0	0	0
0	1	0	0	0	0
1	0	0	0	0	1
1	1	0	0	0	1
0	0	1	0	0	0
0	1	1	0	0	0
1	0	1	0	0	0
1	1	1	0	0	0
0	0	0	1	0	1
0	1	0	1	0	1
1	0	0	1	0	0
1	1	0	1	0	0
0	0	1	1	0	1
0	1	1	1	0	1
1	0	1	1	0	0
1	1	1	1	0	0
0	0	0	0	1	0
0	1	0	0	1	0
1	0	0	0	1	1
1	1	0	0	1	1
0	0	1	0	1	1
0	1	1	0	1	1
1	0	1	0	1	0
1	1	1	0	1	0
0	0	0	1	1	0
0	1	0	1	1	0
1	0	0	1	1	0
1	1	0	1	1	1
0	0	1	1	1	0
0	1	1	1	1	0
1	0	1	1	1	1
1	1	1	1	1	0'''
str_list=data_str.split('\n')
#print(str_list)
for i_str in str_list:
    value=i_str.split('\t')
    i_value=list(map(int,value))
    value_list.append(i_value)
print(prove('(a)&C&D&E|(A)&C&d&E|(A)&c&d&E|(a)&C&D&e|(A)&c&D&e|(a&b)&C&d&e|(a&C)&b&d&e|(a&d)&b&C&e|(a&e)&b&C&d|(b^c)&a&d&e',value_list))