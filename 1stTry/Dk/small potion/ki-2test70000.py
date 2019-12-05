##prototype of finding Dk
##Assume density is 3 and unitary radius is 1


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
N = 90000      ##set 10 for now
txt = 'ala-dip-data_all.txt'
phi, psi = get_pos(txt)
##Dk =[]


##for k in range(1,N):
##    flag
##    Dk = DkSimulator(phi,psi,k,N)
##    if max(Dk)>23.928:
##        break;

NewResult = open('TestNewResult7001.txt','w')



for i in range(70000,80000):
    current = 17          ################################Get this value
    flag = 0
    omega = 4*math.pi /3
    d = 3
    rSort = get_r(i,phi,psi)

    
    while(flag == 0):
        New = current + 1
        Vi = (omega * ((rSort[current][1]))**3)       ##assume d=3
        VjIndex = (rSort[New][0])
        rjSort = get_r(VjIndex-1, phi, psi)
        Vj = (omega * ((rjSort[current][1]))**3)
        if(kiSim(current, Vi,Vj)==0):
            current = New
        else:
            flag = 1
    NewResult.write(str(current) +  ' ' + str(Vi) + " \n")

NewResult.close()

