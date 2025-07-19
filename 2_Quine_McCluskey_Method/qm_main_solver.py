import xlrd
import numpy as np
data=xlrd.open_workbook("C:\Users\lenovo\Downloads\离散数学加分题和规则-1bff7472-1a3e-11ef-8cf7-fa163ef2b19c\真值表.xlsx")
table=data.sheets()[2]
def read(i,j):
    return int(table.cell_value(i,j))
line=1025
row=10
lst=[]
same=[]
vis=[1]*line
cnt=0
cc=0
for i in range(1,line):
    if(int(table.cell_value(i,row))==1):
        lst.append(i)
        cnt+=1
un=0
for i in range(0,row):
    for j in range(i+1,row):
        for l1 in range(0,cnt):
            if(vis[lst[l1]]==0):
                continue
            same.append([(i,j,lst[l1])])
            for l2 in range(l1+1,cnt):
                if(vis[lst[l2]]==0):
                    continue
                for k in range(0,row):
                    if(k==i or k==j):
                        continue
                    if(read(lst[l1],k)!=read(lst[l2],k)):
                        un+=1
                if(un==0):
                        same[cc].append(lst[l2])                   
                        vis[lst[l1]]=vis[lst[l2]]=0
                else:
                    un=0
            cc+=1
l=[0,0,0,0]
myand=[0,0,0,1]
my3=[0,0,1,0]
mya=[0,0,1,1]
my5=[0,1,0,0]
myb=[0,1,0,1]
myxor=[0,1,1,0]
myor=[0,1,1,1]
my2=[1,0,0,0]
myequal=[1,0,0,1]
mynotb=[1,0,1,0]
my4=[1,0,1,1]
mynota=[1,1,0,0]
mycontain=[1,1,0,1]
my1=[1,1,1,0]
all1=[1,1,1,1]

for i in same:
    if(len(i)>1):
        print('(',end='')
        l[read(i[0][2],i[0][0])*2+read(i[0][2],i[0][1])]=1
        now=len(i)-1
        while(now>=1):
            l[read(i[now],i[0][0])*2+read(i[now],i[0][1])]=1
            now-=1
        if(np.equal(l,myor).all()):
            print('(',end='')
            print(chr(97+i[0][0]),end='')
            print('∨',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,myand).all()):
            print('(',end='')
            print(chr(97+i[0][0]),end='')
            print('∧',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,myxor).all()):
            print('(',end='')
            print(chr(97+i[0][0]),end='')
            print('⊕',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,myequal).all()):
            print('(',end='')
            print(chr(97+i[0][0]),end='')
            print('↔',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,mycontain).all()):
            print('(',end='')
            print(chr(97+i[0][0]),end='')
            print('→',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,my1).all()):
            print('(¬',end='')
            print(chr(97+i[0][0]),end='')
            print('∨¬',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,my2).all()):
            print('(¬',end='')
            print(chr(97+i[0][0]),end='')
            print('∧¬',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,my3).all()):
            print('¬(',end='')
            print(chr(97+i[0][0]),end='')
            print('→',end='')
            print(chr(97+i[0][1]),end='')
            print(')',end='')
        if(np.equal(l,my4).all()):
            print('(',end='')
            print(chr(97+i[0][1]),end='')
            print('→',end='')
            print(chr(97+i[0][0]),end='')
            print(')',end='')
        if(np.equal(l,my5).all()):
            print('¬(',end='')
            print(chr(97+i[0][1]),end='')
            print('→',end='')
            print(chr(97+i[0][0]),end='')
            print(')',end='')
        if(np.equal(l,mya).all()):
            print(chr(97+i[0][0]),end='')
        if(np.equal(l,mynota).all()):
            print('¬'+chr(97+i[0][0]),end='')
        if(np.equal(l,myb).all()):
            print(chr(97+i[0][1]),end='')
        if(np.equal(l,mynotb).all()):
            print('¬'+chr(97+i[0][1]),end='')
        ok=0
        if(np.equal(l,all1).all()):
            ok=1
        for k in range(0,row):
            if(k==i[0][0] or k==i[0][1]):
                continue
            if(ok==1):
                ok=0
            else:
                print('∧',end='')
            if(read(i[0][2],k)==0):
                print('¬',end='')
            print(chr(97+k),end='')
        print(')∨',end='')
        l=[0,0,0,0]
for i in range(1,line):
    if(vis[i]==1 and read(i,row)==1):
        print('(',end='')
        for k in range(0,row):
            if(read(i,k)==0):
                print('¬',end='')
            print(chr(97+k),end='')
            if(k!=row-1):
                print('∧',end='')
        print(')∨',end='')
