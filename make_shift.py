import numpy as np
import random
x = np.zeros((1,15,11))
CAN_IN=np.zeros((15,9,11))
count_inoue,count_sato=0,0
S_N=np.zeros((9,11))
lst_1=random.sample(range(11), k=11)
for i in range(0,11):
    lst_1[i]=int(lst_1[i])+4
lst_2=random.sample(range(3), k=3)
for i in range(0,3):
    lst_2[i]=int(lst_2[i])+1
lst_2.append(0)
lst=lst_1+lst_2
shift=np.zeros((9,11))
#  print('lst',lst)
print('シフトパターンを入力してください。ただし早番を1、遅番を2、東部を3、来ない時0とする。')
#  ハマノ　ニシイ　ヤナギダ　ツガワ　ツボ　５　コバヤシ　トリヤ　ミヤハラ　オチアイ　クマイ　１０　コイズミ　シマダ　イノウエ　サトウ　クボタ　１５
#  証明、証明、届け出、届け出、入力、入力、収納、収納、コンシェルジュ、昼休憩
#  早番を1、遅番を2、東部を3、来ない時0とする
a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,b6,b7,c1,c2,c3=input().split()
abc=[int(a1),int(a2),int(a3),int(a4),int(a5),int(b1),int(b2),int(b3),int(b4),int(b5),int(b6),int(b7),int(c1),int(c2),int(c3),]
#  昼休みに入る人を把握
H_N=0
for i in range(0,15):
    if (abc[i]==1) or (abc[i]==2):
        H_N+=1
print('今日休憩するべき人数',H_N)
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
L_E=[]
L_M=[]
L_L=[]
temp=(len(Normal)+len(Emproyee))//3
L_E.append(Emproyee[0])
L_M.append(Emproyee[1]) 

for i in range(0,temp-1):
    L_E.append(Normal[i])

for i in range(0,temp-1):
    L_M.append(Normal[temp-1+i])

for i in range(0,len(Emproyee)-2):
    L_L.append(Emproyee[2+i])
for i in range(len(Normal)-2*(temp-1)+1,len(Normal)):
    L_L.append(Normal[i])



print('L_E',L_E,'L_M',L_M,'L_L',L_L)


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
#  print('x',x)
#  np.savetxt('c:/Users/m_tsugawa/Documents/Python_Scripts/np_savetxt.txt', x)
for i in range(0,15):
    CAN_IN[i,0:9,0:11]=x[0,i,0:11]
#  print(CAN_IN)

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
for i in range(0,len(L_E)):
    CAN_IN[L_E[i],:,4]=0
for i in range(0,len(L_M)):
    CAN_IN[L_M[i],:,5]=0
for i in range(0,len(L_L)):
    CAN_IN[L_L[i],:,6]=0


#  仕事の代入優先順位を決定(Priority)
P_W=[0,1,2,3,4,5,6,7]
for j in [0,1,2,3]:
    random.shuffle(P_W)
    #  print('j',j)
    for i in range(0,8):
        for k in range(0,15):
            if CAN_IN[lst[k],P_W[i],j]==1:
                #  print('task1',lst[k],P_W[i],j)
                shift[P_W[i],j]=lst[k]
                CAN_IN[lst[k],:,j]=0
                if (j!=0)and((P_W[i]==0)or(P_W[i]==1))and((shift[0,j-1]==shift[P_W[i],j]) or (shift[1,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],0,j+1]=0
                    CAN_IN[lst[k],1,j+1]=0
                if (j!=0)and((P_W[i]==2)or(P_W[i]==3))and((shift[2,j-1]==shift[P_W[i],j]) or (shift[3,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],2,j+1]=0
                    CAN_IN[lst[k],3,j+1]=0
                #  サトウ、イノウエは照明と届け出が合計４まで
                if lst[k]==12:
                    count_inoue+=1
                if lst[k]==13:
                    count_sato+=1
                if count_inoue>=4:
                    CAN_IN[12,1:5,:]=0
                if count_sato>=4:
                    CAN_IN[13,1:5,:]=0
                break

P_W_L=[0,2,6]
SP_W_L=[1,3]
NP_W_L=[4,5,7]
for j in [4,5,6]:
    random.shuffle(P_W_L)
    random.shuffle(SP_W_L)
    random.shuffle(NP_W_L)
    P_W=P_W_L + SP_W_L + NP_W_L
    #  print('j',j)
    for i in range(0,8):
        for k in range(0,15):
            if CAN_IN[lst[k],P_W[i],j]==1:
                #  print('task1',lst[k],P_W[i],j)
                shift[P_W[i],j]=lst[k]
                CAN_IN[lst[k],:,j]=0
                if (j!=0)and((P_W[i]==0)or(P_W[i]==1))and((shift[0,j-1]==shift[P_W[i],j]) or (shift[1,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],0,j+1]=0
                    CAN_IN[lst[k],1,j+1]=0
                if (j!=0)and((P_W[i]==2)or(P_W[i]==3))and((shift[2,j-1]==shift[P_W[i],j]) or (shift[3,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],2,j+1]=0
                    CAN_IN[lst[k],3,j+1]=0
                #  サトウ、イノウエは照明と届け出が合計４まで
                if lst[k]==12:
                    count_inoue+=1
                if lst[k]==13:
                    count_sato+=1
                if count_inoue>=4:
                    CAN_IN[12,1:5,:]=0
                if count_sato>=4:
                    CAN_IN[13,1:5,:]=0
                break

P_W=[0,1,2,3,4,5,6,7]
for j in [7,8,9,10]:
    random.shuffle(P_W)
    #  print('j',j)
    for i in range(0,8):
        for k in range(0,15):
            if CAN_IN[lst[k],P_W[i],j]==1:
                #  print('task1',lst[k],P_W[i],j)
                shift[P_W[i],j]=lst[k]
                CAN_IN[lst[k],:,j]=0
                if (j!=10)and((P_W[i]==0)or(P_W[i]==1))and((shift[0,j-1]==shift[P_W[i],j]) or (shift[1,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],0,j+1]=0
                    CAN_IN[lst[k],1,j+1]=0
                if (j!=10)and((P_W[i]==2)or(P_W[i]==3))and((shift[2,j-1]==shift[P_W[i],j]) or (shift[3,j-1]==shift[P_W[i],j])):
                    CAN_IN[lst[k],2,j+1]=0
                    CAN_IN[lst[k],3,j+1]=0
                #  サトウ、イノウエは照明と届け出が合計４まで
                if lst[k]==12:
                    count_inoue+=1
                if lst[k]==13:
                    count_sato+=1
                if count_inoue>=4:
                    CAN_IN[12,1:5,:]=0
                if count_sato>=4:
                    CAN_IN[13,1:5,:]=0
                break


print('shift')
print(shift)     

S_N=np.zeros((9,11), dtype='<U5')           
for i in range(0,9):
    for j in range(0,11):
        if shift[i,j]==0:
            S_N[i,j]='未代入　　'
        if shift[i,j]==1:
            S_N[i,j]='ニシイ　　'
        if shift[i,j]==2:
            S_N[i,j]='ヤナギダ　'
        if shift[i,j]==3:
            S_N[i,j]='ツガワ　　'
        if shift[i,j]==4:
            S_N[i,j]='ツボ　　　'
        if shift[i,j]==5:
            S_N[i,j]='コバヤシ　'
        if shift[i,j]==6:
            S_N[i,j]='トリヤ　　'
        if shift[i,j]==7:
            S_N[i,j]='ミヤハラ　'
        if shift[i,j]==8:
            S_N[i,j]='オチアイ　'
        if shift[i,j]==9:
            S_N[i,j]='クマイ　　'
        if shift[i,j]==10:
            S_N[i,j]='コイズミ　'
        if shift[i,j]==11:
            S_N[i,j]='シマダ　　'
        if shift[i,j]==12:
            S_N[i,j]='イノウエ　'
        if shift[i,j]==13:
            S_N[i,j]='サトウ　　'
        if shift[i,j]==14:
            S_N[i,j]='クボタ　　'
print('S_N')
print(S_N)

np.savetxt('c:/Users/m_tsugawa/Documents/Github/S_N.csv', S_N,fmt='%s',delimiter=',')
