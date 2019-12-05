##Calculate Free Energy for each point
##Fix d = 3 to d = 2
##Not sure d = 2 but calculate with this for Fcalc2
## Fix log to log10
import math



def get_pos(txt):
    phi = []
    psi =[]
    original = open(txt, 'r')      ##Use this for now

    for line in original.readlines():     ##get phi and psi
        OneLine = line.split(' ')
        phi.append(float(OneLine[0]))
        psi.append(float(OneLine[1]))
    original.close()
    return phi, psi

def get_ki_Vi(txt):
    ki = []
    Vi = []
    result = open(txt,'r')
    for line in result.readlines():
        OneLine = line.split(' ')
        ki.append(int(OneLine[0]))
        Vi.append(float(OneLine[1]))
    result.close()
    return ki, Vi
        
def get_r(i,phi,psi):
    r = {}
    for j in range(0,N):    ##to determine the length
        r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))
    rSort= sorted(r.items(), key=lambda x:x[1])

    
    return rSort

##original = open('ala-dip-data_all.txt', 'r')      ##Use this for now
##ki = open('Dk_whole.txt','r')
NewResult = open('Energy.txt','a')


txt = 'ala-dip-data_all.txt'
phi, psi = get_pos(txt)
##omega = math.pi
##d = 2
N = 100                        ##Put whatever the value you have in text data
txt2 = 'NewResult.txt'
ki, Vi= get_ki_Vi(txt2)
##Main
for i in range (0,N):
##    rSort = get_r(i,phi,psi)
    F = -math.log10(ki[i]/Vi[i])
    NewResult.write(str(phi[i]) + " " + str(psi[i]) + " " + str(round(F,11)) + " \n")
NewResult.close()
