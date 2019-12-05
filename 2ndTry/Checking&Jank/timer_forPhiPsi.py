##Timer 
import timeit, math

phi = []
psi =[]
r = []
l = 90000        ##choose l, total value

Result = open('ala-dip-data_all.txt', 'r')      ##Use this for now
start = timeit.default_timer()
for line in Result.readlines():     ##get phi and psi
    OneLine = line.split(' ')
    phi.append(float(OneLine[0]))
    psi.append(float(OneLine[1]))

##for i in range(0,500):        ##from 0 to l number
##    for j in range(0,l):    ##to determine the length
##        r.append(math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2)))            ##Get r for every value
##    r.sort()                                                                        ##sort r values
##    r.pop(0)                                                                        ##pop the first value since the first one should have i=j and r
##    r = r*0
##Result.close()

R = []

for i in range(0,500):        ##from 0 to l number
    for j in range(0,l):    ##to determine the length
        deltaPhi = phi[i]-phi[j]
        deltaPsi = psi[i]-psi[j]
        if deltaPhi > 180:
            deltaPhi = 180-deltaPhi%180
        if deltaPsi > 180:
            deltaPsi = 180-deltaPsi%180 
        r.append(math.sqrt(((deltaPhi)**2) + ((deltaPsi)**2)))            ##Get r for every value
    r.sort()                                                                        ##sort r values
    r.pop(0)                                                                        ##pop the first value since the first one should have i=j and r
    r = r*0
stop = timeit.default_timer()
print(stop-start)
Result.close()
