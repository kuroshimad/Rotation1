##Remoddeling of Dk simulator. Do not append Dk, whenever it hit 23.928, it stops. 


import math
import copy

def DkSimulator(phi,psi,k,N):

    r = {}
    omega = math.pi
    d = 2


    Vi = []
    Vj = []
    VjIndex = []
    Dk = []

    for i in range(0,N):        ##from 0 to N
        for j in range(0,N):    ##to determine the length
            r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))
        rSort= sorted(r.items(), key=lambda x:x[1])

        Vi.append(omega * ((rSort[k][1])**d))       ##assume d=2
        VjIndex.append(rSort[k+1][0])
        r = {}
    for i in VjIndex:
        Vj.append( Vi[i-1])         ##i-1 since Vi start from 0 and VjIndex start from 1


    flag = 0
    for i in range (0,N):
        if ((-2*k*math.log((4*Vi[i]*Vj[i])/((Vi[i]+Vj[i])**2)))>23.928):
            flag = 1
            break
    return flag


##Main


N = 90000      ##set 10 for now
Dk =[]
phi = []
psi =[]
Result = open('ala-dip-data_all.txt', 'r')      ##Use this for now

for line in Result.readlines():     ##get phi and psi
    OneLine = line.split(' ')
    phi.append(float(OneLine[0]))
    psi.append(float(OneLine[1]))
Result.close()

#for k in range(1,N):
flag = DkSimulator(phi,psi,100,N)
 #   if (Dk == 1):
  #      break
print(k-1)



