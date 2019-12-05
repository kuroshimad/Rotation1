##the result does not look like a line

import math
import copy

phi = []
psi =[]
r = []
originalMiu={}
sigma = []
l = 2000        ##get l, total value
Result = open('ala-dip-data.txt', 'r')      ##Use this for now
density = open('density.txt','w')



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




miu = sorted(originalMiu.items(), key=lambda x:x[1])


for i in range (0,l):
    sigma.append(miu[i][0])

for i,j in originalMiu.items():
    density.write(str(math.log(j)) +' ' + str(-math.log(1-(sigma[i])/l)) + '\n')    ##if i add 1, math domain error by log(0)
    

density.close()



##    for m in range(0,k):     ##size of k, finding V
##        v[m] = omega(r[m]**d + r[m-1]**d)
##        
##    V[i] = sum(v)
