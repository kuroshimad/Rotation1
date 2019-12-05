##not working well since some miu are equal to each other. ver2 will use dictionary form instead



import math
import copy

phi = []
psi =[]
r = []
originalMiu=[]
sigma = []
miu = []
l = 1000        ##get l, total value
Result = open('ala-dip-data.txt', 'r')      ##Use this for now
density = open('density.txt','w')
for line in Result.readlines():
    OneLine = line.split(' ')
    phi.append(float(OneLine[0]))
    psi.append(float(OneLine[1]))
Result.close()

for i in range(0,l):        ##from 0 to l number
    for j in range(0,l):    ##to determine the length
        r.append(math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2)))
    r.sort()
    r.pop(0)
    miu.append(r[1]/r[0])
    r = []
originalMiu = copy.deepcopy(miu)
miu.sort()


for i in miu:
    sigma.append(originalMiu.index(i))

for i in range (0,l):
    density.write(str(math.log(originalMiu[i])) +' ' + str(-math.log(1-sigma[i]/l)) + '\n') 


density.close()



##    for m in range(0,k):     ##size of k, finding V
##        v[m] = omega(r[m]**d + r[m-1]**d)
##        
##    V[i] = sum(v)
