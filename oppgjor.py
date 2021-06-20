import numpy as np
from collections import Counter



def totalt_i_kassa(tusen = 0, fem_hundre = 0, to_hundre = 0, ett_hundre = 0, femti = 0, tjue = 0, ti = 0, fem = 0, en = 0):

    kontant_liste = [1000,500,200,100,50,20,10,5,1]

    tusen *= 1000
    fem_hundre *= 500
    to_hundre *= 200
    ett_hundre *= 100
    femti *= 50
    tjue *= 20
    ti *= 10
    fem *= 5

    kassa = Counter({'1000': tusen, '500': fem_hundre, '200': to_hundre, \
    '100': ett_hundre, '50': femti, '20': tjue, '10': ti, '5': fem, '1': en})

    total_sum = sum(kassa.values())

    print ('sum totalt før utregninger', total_sum)

    kassa_totalt = 1500
    posen_totalt = total_sum - kassa_totalt

    posen = Counter({})
    print ('i posen skal det være' , posen_totalt, 'kr')

    #ind the optimal slution using the least amount of coins for the bag
    for i in kontant_liste:
        print ('---------------------------------------------')
        print ('i = ', i)
        i_sum = posen_totalt//i
        print ('heltallsdiisjon ',i_sum)

        remainder = kassa[str(i)]/i - i_sum
        print ('remainder' , remainder)

        if remainder > 0:
            print ('result was bigger than 0')
            posen[str(i)] = i_sum * i
            print (posen[str(i)])

            #oppdatere  resterende sum
            posen_totalt -= i_sum * i

            #oppdatere beløp i kassa
            kassa[str(i)] -= i_sum*i


        else:
            print ('result was smaller than 0')
            posen[str(i)] = kassa[str(i)]

            #oppdatere  resterende sum
            posen_totalt -= kassa[str(i)]

            #oppdatere beløp i kassa
            kassa[str(i)] = 0
    print ('\nPOSEN')
    print ([posen[str(i)]/i for i in kontant_liste])
    print(sum(posen.values()))
    print ('\nKASSA')

    print ([kassa[str(i)]/i for i in kontant_liste])
    print(sum(kassa.values()))

# if kassa != 1500 noe gikk galt

totalt_i_kassa(3,2,5,3,15,10,4,12,32)
