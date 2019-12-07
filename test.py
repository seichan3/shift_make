
import numpy as np
import random
'''
x = np.zeros((1,15,11))
CAN_IN=np.zeros((15,9,11))
count_inoue,count_sato=0,0
lst_1=random.sample(range(11), k=11)
for i in range(0,11):
    lst_1[i]=int(lst_1[i])+4
lst_2=random.sample(range(3), k=3)
for i in range(0,3):
    lst_2[i]=int(lst_2[i])+1
lst_2.append(0)
lst=lst_1+lst_2
shift=np.zeros((9,11))
print('シフトパターンを入力してください。ただし早番を1、遅番を2、東部を3、来ない時0とする。')
#  ハマノ　ニシイ　ヤナギダ　ツガワ　ツボ　５　コバヤシ　トリヤ　ミヤハラ　オチアイ　クマイ　１０　コイズミ　シマダ　イノウエ　サトウ　クボタ　１５
#  証明、証明、届け出、届け出、入力、入力、収納、収納、コンシェルジュ、昼休憩
#  早番を1、遅番を2、東部を3、来ない時0とする
a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,b6,b7,c1,c2,c3=input().split()
abc=[int(a1),int(a2),int(a3),int(a4),int(a5),int(b1),int(b2),int(b3),int(b4),int(b5),int(b6),int(b7),int(c1),int(c2),int(c3),]
print('コンジェルジュABCDの順に数字にて入力してください、また、濱田さんが居れば1そうでなければ0を入力してください')
#  昼休みに入る人を把握
H_N=0
for i in range(0,15):
    if (abc[i]==1) or (abc[i]==2):
        H_N+=1
print(H_N)
#  契約社員、社員で早く、遅く入っている人を把握、ランダム化
Early_Normal=[]
Lately_Normal=[]
Early_Emproyee=[]
Lately_Emproyee=[]
for i in range(5,15):
    if abc[i]==1:
        Early_Normal.append(i)
    if abc[i]==2:
        Lately_Normal.append(i)
for i in range(0,5):
    if abc[i]==1:
        Early_Emproyee.append(i)
    if abc[i]==2:
        Lately_Emproyee.append(i)
random.shuffle(Early_Normal)
random.shuffle(Lately_Normal)
random.shuffle(Early_Emproyee)
random.shuffle(Lately_Emproyee)
Normal=Early_Normal+Lately_Normal
Emproyee=Early_Emproyee+Lately_Emproyee
#  誰が休憩に入るか(Lunch_Early,Middle,Lately)
temp=(len(Normal)+len(Emproyee))//3
print(temp)
L_E=[]
L_M=[]
L_L=[]
L_E.append(Emproyee[0])
L_M.append(Emproyee[1]) 

for i in range(0,temp-1):
    L_E.append(Normal[i])

for i in range(0,temp-1):
    L_M.append(Normal[temp-1+i])

for i in range(0,len(Emproyee)-2):
    L_L.append(Emproyee[2+i])
for i in range(len(Normal)-2*(temp-1)+1,len(Normal)):
    print('i')
    print(i)
    L_L.append(Normal[i])

print('L_E',L_E)
print(L_M) 
print(L_L)
y=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(L_E)):
    y[L_E[i]]=1
print(y)
'''
xx=np.zeros((5,5), dtype='<U5')
for i in range(0,3):
    for j in range(0,4):
        if (i==2)and(j==1):
            xx[i,j]='test'

print(xx)
print('tesjdkcs　　　え')