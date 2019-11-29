import numpy as np
import random
np.set_printoptions(threshold=30)
x = np.zeros((1,15,11))
CAN_IN=np.zeros((15,9,11))
count_inoue,count_sato=0,0
lst_1=random.sample(range(11), k=11)
for i in range(0,11):
    lst_1[i]=int(lst_1[i])+4
lst_2=random.sample(range(3), k=3)
for i in range(0,3):
    lst_2[i]=int(lst_2[i])+1
lst=lst_1+lst_2
lst.append(0)
print('シフトパターンを入力してください。ただし早番を1、遅番を2、東部を3、来ない時0とする。')
#  ハマノ　ニシイ　ヤナギダ　ツガワ　ツボ　５　コバヤシ　トリヤ　ミヤハラ　オチアイ　クマイ　１０　コイズミ　シマダ　イノウエ　サトウ　クボタ　１５
a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,b6,b7,c1,c2,c3=input().split()
abc=[int(a1),int(a2),int(a3),int(a4),int(a5),int(b1),int(b2),int(b3),int(b4),int(b5),int(b6),int(b7),int(c1),int(c2),int(c3),]
#  print(ABC)
#  早番を1、遅番を2、東部を3、来ない時0とする
print('コンジェルジュABCDの順に数字にて入力してください、また、濱田さんが居れば1そうでなければ0を入力してください')
A,B,C,D,H=input().split()
ABCDH=[int(A),int(B),int(C),int(D),int(H)]

for i in range(0,15):
    I=int(abc[i])
    if I==1:
        x[0,i,:8]=1
    elif I==2:
        x[0,i,2:11]=1
    elif I==3:
        x[0,i,7:11]=1 
print(x)
#  np.savetxt('c:/Users/m_tsugawa/Documents/Python_Scripts/np_savetxt.txt', x)
for i in range(0,15):
    CAN_IN[i,:,0:11]=x[0,i,0:11]
#  print(CAN_IN)
shift=np.zeros((9,11))

#  臨時職員はコンシェルジュに入れない
CAN_IN[12:14,8,:]=0

#  時短勤務 サトウ、クボタ
if abc[13]==1:
    CAN_IN[13,:,8]=0
elif abc[13]==2:
    CAN_IN[13,:,2]=0
if abc[14]==1:
    CAN_IN[14,:,0]=0
#  コンシェルジュ代入
if ABCDH[4]==1:
    for idx in [4,8]:
        shift[8,idx] = 14
    for idx in [0,2]:
        shift[8,idx] = ABCDH[0]
    for idx in [1,5]:
        shift[8,idx] = ABCDH[1]
    for idx in [3,6]:
        shift[8,idx] = ABCDH[2]
    for idx in [7]:
        shift[8,idx] = ABCDH[3]    
else :
    for idx in [0,2,6]:
        shift[8,idx] = ABCDH[0]
    for idx in [1,3]:
        shift[8,idx] = ABCDH[1]
    for idx in [4,7]:
        shift[8,idx] = ABCDH[2]
    for idx in [5,8]:
        shift[8,idx] = ABCDH[3]   
for i in range(0,9):
    for j in range(0,11):
        if shift[i,j]!=0:
            I=int(shift[i,j])
            CAN_IN[I,:,j]=0

print(shift)



#  サトウ、イノウエは照明と届け出が合計４まで
'''
for i in range(0:9):
    for j in range(0:11):
        if shift[i,j]=13:
            count_sato
'''

if count_inoue>=4:
    CAN_IN[12,1:5,:]=0
if count_sato>=4:
    CAN_IN[13,1:5,:]=0

