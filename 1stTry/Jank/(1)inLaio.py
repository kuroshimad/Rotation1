import math



Result = open('ala-dip-data.txt', 'r')      ##Use this for now

phi = []
psi =[]
r = []
v = []
V = []
d =         ##find d!!!!!
omega =     ##find omega!!
for line in Result.readlines():
    OneLine = line.split(' ')
    phi.append(OneLine[0])
    psi.append(OneLine[1])
Result.close()

l = len(phi) ##total vlue



for i in range(0,l):        ##from 0 to l number
    for j in range(0,l):    ##to determine the length
        r[j] = math.sqrt(((phi[j]-phi[j+1])**2) + ((psi[j]-psi[j+1])**2))   ##includes itself which becomes 0
            
    r.sort()
    
    for m in range(0,k):     ##size of k, finding V
        v[m] = omega(r[m]**d + r[m-1]**d)
        
    V[i] = sum(v)
    
    
Dk = -2*k*(math.log(V)+math.log(Vj)-2*math.log(V+Vj)+math.log(4))  ##Does not need omega

