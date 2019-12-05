## care periodic boundry

###In this program, we calculate small d. d is the dimension of the manifold
### We determine d by TWO-NN methods.
##Fix log to log10
import math
import copy

phi = []
psi =[]
r = []
originalMiu={}
l = 90000        ##choose l, total value

Result = open('ala-dip-data_all.txt', 'r')      ##Use this for now
density = open('TESTtestdensity.txt','w')

for line in Result.readlines():     ##get phi and psi
    OneLine = line.split(' ')
    phi.append(float(OneLine[0]))
    psi.append(float(OneLine[1]))
Result.close()

for i in range(0,l):        ##from 0 to l number
    for j in range(0,l):    ##to determine the length
        deltaPhi = phi[i]-phi[j]                                                    ##care periodic boundry
        deltaPsi = psi[i]-psi[j]                                                    ##care periodic boundry
        if deltaPhi > 180:
            deltaPhi = 180-deltaPhi%180
        if deltaPsi > 180:
            deltaPsi = 180-deltaPsi%180 
        r.append(math.sqrt(((deltaPhi)**2) + ((deltaPsi)**2)))                      ##Get r for every value
    r.sort()                                                                        ##sort r values
    r.pop(0)                                                                        ##pop the first value since the first one should have i=j and r = 0. 
    originalMiu[i] = r[1]/r[0]
    r = []

miu = sorted(originalMiu.items(), key=lambda x:x[1])    ##sorting by accending order of originalMiu value

for i in range(0,l):        ##getting log(miui), log(1-Femp(miui))
    density.write(str(miu[i][1])+ '\n')    ##if I add 1, math domain error by log(0)
    

density.close()



