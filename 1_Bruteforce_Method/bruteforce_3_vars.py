import itertools

def all_sorts(lst):
    return [''.join(p) for p in itertools.permutations(lst)]
def create_order():
    letters_list=[]
    for i1 in ('a','A'):
        for i2 in ('b','B'):
            for i3 in ('c','C'):
                m_list=[i1,i2,i3]
                letter_list=all_sorts(m_list)
                letters_list+=letter_list
    order_list=[]
    for letter in letters_list:
        for i in ('&','|'):
            for j in ('&','|'):
                t_str='('+letter[0]+i+letter[1]+')'+j+letter[2]
                order_list.append(t_str)
    return order_list
def prove(shi,value_list):
    flag=1
    for value in value_list:
        a=value[0]
        b=value[1]
        c=value[2]
        A=a^1
        B=b^1
        C=c^1
        if not eval(shi)==value[3]:
            flag=0
            break
    if flag==0:
        return  False
    elif flag==1:
        return True

order_list=create_order()
value_list=[]
count=0
data_str='''0	0	0	0
0	1	0	0
1	0	0	1
1	1	0	1
0	0	1	0
0	1	1	1
1	0	1	0
1	1	1	1'''
str_list=data_str.split('\n')
#print(str_list)
for i_str in str_list:
    value=i_str.split('\t')
    i_value=list(map(int,value))
    value_list.append(i_value)
for order in order_list:
    if(prove(order,value_list)==True):
       print(order)
    

