##prototype of finding Dk
##Assume density is 3 and unitary radius is 1


import math
import copy


def get_pos(txt): 			## get phi and psi from the text data 
    phi = []
    psi =[]
    Result = open(txt, 'r')      	##open txt file

    for line in Result.readlines():     ##get one line each time
        OneLine = line.split(' ')       ##separate words by space
        phi.append(float(OneLine[0]))   ##get phi
        psi.append(float(OneLine[1]))   ##get psi
    Result.close()
    return phi, psi			##return lists of all phi and psi

def get_r(i,phi,psi):			                                ##get radius in ascending order with originl position
    r = {}                                                              ##r would be original position1: radius1, original position2:radius2......
    for j in range(0,N):    		                                ##determine the length
        r[j] = math.sqrt(((phi[i]-phi[j])**2) + ((psi[i]-psi[j])**2))   ##euclidian distance        ##Includes i itself
    rSort= sorted(r.items(), key=lambda x:x[1])                         ##sorted by the radius

    
    return rSort			                                ##return all radius from point i to others in dictionary form


def kiSim(k, Vi, Vj):					##check Dk value exceeds 23.928 or not
    Dk = (-2*k*math.log((4*Vi*Vj)/((Vi+Vj)**2)))	##how to get Dk value. Check notebook how Eq 3 goes this formula.
    if(Dk>23.928):                                      ##Maybe I can do in this way... return Dk//23.928.  This would be a little bit faster 
        return 1
    else:
        return 0


##Main
N = 90000      				##able to change the total number to whatever the number you want to explore, but do not exceed the maximum
txt = 'ala-dip-data_all.txt'            ##data we read
phi, psi = get_pos(txt)


NewResult = open('NewResult.txt','w')



for i in range(0,N):
    current = 1          ################################This is k. Get this value from Dk.py.  If not, strat from 1
    flag = 0				##When Dk < 23.928 but Dk+1 > 23.928, flag = 1
    omega = math.pi			##since it is two dimentional
    d = 2				##two dimention
    rSort = get_r(i,phi,psi)		##get sorted radius for each i 

    
    while(flag == 0):
        New = current + 1               ##k+1
        Vi = (omega * ((rSort[current][1]))**d)		##current start from 1 since you should not include index 0 which is ownself
        VjIndex = (rSort[New][0])			##this is just an index of Vj, which means k+1.             ##j is the index of the k+1 which is written as new
        rjSort = get_r(VjIndex-1, phi, psi)		##I know this is confusing. VjIndex-1 since i started from 0 to N but current start from 1. So There is a different. 
        Vj = (omega * ((rjSort[current][1]))**d)        ##Checked **d calculate first 
        if(kiSim(current, Vi,Vj)==0):
            current = New
        else:
            flag = 1
    NewResult.write(str(current) +  ' ' + str(Vi) + " \n")		##Print ki and Vi

NewResult.close()

