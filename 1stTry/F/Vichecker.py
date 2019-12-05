##Calculate Free Energy for each point
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

def get_ki(txt):
    ki = []
    result = open(txt,'r')
    for line in result.readlines():
        OneLine = line.split(' ')
        ki.append(int(OneLine[0]))
    result.close()
    return ki
        
def get_r(i,phi,psi):
    r = {}
    for j in range(0,N):    ##to determine the length
        r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))
    rSort= sorted(r.items(), key=lambda x:x[1])

    
    return rSort

original = open('ala-dip-data_all.txt', 'r')      ##Use this for now
ki = open('Dk_whole.txt','r')
NewResult = open('checingVi.txt','a')


txt = 'ala-dip-data_all.txt'
phi, psi = get_pos(txt)
omega = 4*math.pi /3
d = 3
N = 90000
txt2 = 'Dk_whole.txt'
ki = get_ki(txt2)
##Main
for i in range (0,N):
    rSort = get_r(i,phi,psi)
    Vi = (omega * ((rSort[ki[i]][1]))**3)
#    F = -math.log(ki[i]/Vi)
    NewResult.write(str(Vi) + " \n")
NewResult.close()
