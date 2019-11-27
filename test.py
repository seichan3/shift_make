import numpy as np
np.set_printoptions(threshold=30)
x = np.zeros((1,15,11))
CAN_IN=np.zeros((15,9,11))

print('シフトパターンを入力してください。ただし早番を1、遅番を2、東部を3、来ない時0とする。')
a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,b6,b7,c1,c2,c3=input().split()
abc=[int(a1),int(a2),int(a3),int(a4),int(a5),int(b1),int(b2),int(b3),int(b4),int(b5),int(b6),int(b7),int(c1),int(c2),int(c3),]
# print(ABC)
#早番を1、遅番を2、東部を3、来ない時0とする#
print('コンジェルジュABCDの順に数字にて入力してください、また、濱田さんが居れば1そうでなければ0を入力してください')
A,B,C,D,H=input().split()
ABCDH=[int(A),int(B),int(C),int(D),int(H)]

for i in range(0,15):
    I=int(abc[i])
    if I==1:
        x[0,i,0:8]=1
    elif I==2:
        x[0,i,2:11]=1
    elif I==3:
        x[0,i,7:11]=1 
print(x)
#  np.savetxt('c:/Users/m_tsugawa/Documents/Python_Scripts/np_savetxt.txt', x)

for i in range(0,15):
    CAN_IN[i,:,0:11]=x[0,i,0:11]

print(CAN_IN)