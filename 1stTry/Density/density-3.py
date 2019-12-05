##sophisticated version of density-2-1.py
import math
import copy

phi = []
psi =[]
r = []
originalMiu={}
l = 11000        ##choose l, total value

Result = open('ala-dip-data_all.txt', 'r')      ##Use this for now
density = open('testdensity.txt','w')

for line in Result.readlines():     ##get phi and psi
    OneLine = line.split(' ')
    phi.append(float(OneLine[0]))
    psi.append(float(OneLine[1]))
Result.close()

for i in range(0,l):        ##from 0 to l number
    for j in range(0,l):    ##to determine the length
        r.append(math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2)))
    r.sort()
    r.pop(0)
    originalMiu[i] = r[1]/r[0]
    r = []

miu = sorted(originalMiu.items(), key=lambda x:x[1])    ##sorting by accending order of originalMiu value

for i in range(0,l):        ##getting log(miui), log(1-Femp(miui))
    density.write(str(math.log(miu[i][1])) +' ' + str(-math.log(1-(i)/l)) + '\n')    ##if I add 1, math domain error by log(0)
    

density.close()



