##prototype of finding Dk
##Assume density is 3 and unitary radius is 1


import math
import copy

def DkSimulator(phi,psi,k,N):

    r = {}
    omega = 4*math.pi /3
    d = 3


    Vi = []
    Vj = []
    VjIndex = []
    Dk = []

    for i in range(0,N):        ##from 0 to N
        for j in range(0,N):    ##to determine the length
            r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))
        rSort= sorted(r.items(), key=lambda x:x[1])

        Vi.append(omega * ((rSort[k][1]))**3)       ##assume d=3
        VjIndex.append(rSort[k+1][0])
        r = {}
    for i in VjIndex:
        Vj.append( Vi[i-1])         ##i-1 since Vi start from 0 and VjIndex start from 1

    for i in range (0,N):
        Dk.append(-2*k*math.log((4*Vi[i]*Vj[i])/((Vi[i]+Vj[i])**2)))
    return Dk


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

for k in range(1,N):
    Dk = DkSimulator(phi,psi,k,N)
    if max(Dk)>23.928:
        break
print(k)



