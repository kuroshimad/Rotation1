import math

##i = 9 ## equal to total data point 
F = 1.12345678987456321 ## Free Energy, What we need to find in this program

Result = open('ala-dip-data.txt', 'r')
NewResult = open('NewResult.txt','w')

for line in Result.readlines():
    OneLine = line.split(' ')
    first = OneLine[0]
    second = OneLine[1]
    ##And do wehatever the calculation you need for F
##    for i in k:
##        F = -math.log(k/V)


    NewResult.write(first + " " + second + " " + str(round(F,11)) + " \n")
    
    
Result.close()
NewResult.close()


##
##omega = 
##r[] =         ##all the r values
##k =       ##optimal number of neigthbor
##d =       ##dimension
##for j in l:
##    if j ==1:
##        v = omega*(r[j]**d)
##    else:
##        v = omega*(r[j]**d-r[j-1]**d)      ##Don't forget to add 0 in the begining of r
##    V = V + v
##p = ##ρ
##L = k *math.log(p) - pV           ##log liklihood
##


##Dk = -2*k*(math.log(V)+math.log(Vj)-2*math.log(V+Vj)+math.log(4))

