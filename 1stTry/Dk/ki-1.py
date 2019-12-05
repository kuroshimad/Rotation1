##prototype of finding Dk
##Assume density is 3 and unitary radius is 1
##Failed since Vj did not change

import math
import copy


def get_pos(txt):
    phi = []
    psi =[]
    Result = open(txt, 'r')      ##Use this for now

    for line in Result.readlines():     ##get phi and psi
        OneLine = line.split(' ')
        phi.append(float(OneLine[0]))
        psi.append(float(OneLine[1]))
    Result.close()
    return phi, psi

def get_r(i,phi,psi):
    r = {}
    for j in range(0,N):    ##to determine the length
        r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))
    rSort= sorted(r.items(), key=lambda x:x[1])

    
    return rSort


def kiSim(k, Vi, Vj):
    Dk = (-2*k*math.log((4*Vi*Vj)/((Vi+Vj)**2)))
    if(Dk>23.928):
        return 1
    else:
        return 0


##Main
N = 2000      ##set 10 for now
txt = 'ala-dip-data.txt'
phi, psi = get_pos(txt)
##Dk =[]


##for k in range(1,N):
##    flag
##    Dk = DkSimulator(phi,psi,k,N)
##    if max(Dk)>23.928:
##        break;

NewResult = open('NewResult.txt','w')



for i in range(0,N):
    current = 1          ################################Get this value
    flag = 0
    omega = 4*math.pi /3
    d = 3
    rSort = get_r(i,phi,psi)
    Vi = (omega * ((rSort[current][1]))**3)       ##assume d=3
    VjIndex = (rSort[current+1][0])
    rjSort = get_r(VjIndex, phi, psi)
    Vj = (omega * ((rjSort[current][1]))**3)
    while(flag == 0):
        New = current + 1
        if(kiSim(New, Vi,Vj)==0):
            current = New
        else:
            flag = 1
    NewResult.write(str(current) +  ' ' + str(Vi) + " \n")

NewResult.close()

