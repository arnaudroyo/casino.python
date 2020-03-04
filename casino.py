# a = random.randint(1,2)
# if a == 1:
#     print("ok")
# else:
#     print("nop")

import random
import time

pot = 0
while pot <= 0 or pot > 10000:
    try:
        pot = int(input("Quel est votre pot de départ ?"))
        assert pot > 0 and pot < 10000
    except AssertionError:
        print("Veuillez rentrer un nombre supérieur à 0 et inférieur à 10000")
    except ValueError:
        print("Veuillez rentrer un nombre")
        pot = 0
    
print("Vous commencer avec ", pot,"€")

while pot > 0:
    case = -1
    while case <=0 or case >50:
        try:
            case = int(input("Misez sur un nombre entre 1 et 50:"))
            assert case > 0 and case < 50
        except AssertionError:
            print("Veuillez rentrer un nombre supérieur à 0 et inférieur à 50")
        except ValueError:
            print("Veuillez rentrer un nombre")

    mise = -1        
    while mise <=0 or mise > pot:
        try:
            mise = int(input("Misez un montant de votre pot:"))
            assert mise > 0 and mise < pot
        except AssertionError:
            print("Veuillez rentrer un nombre supérieur à 0 et inférieur à ", pot)
        except ValueError:
            print("Veuillez rentrer un nombre")

    print("Vous avez misé ", mise,"€ sur la case ", case,",Bonne chance !")
    time.sleep(2)
    print("ça tourne")    
    res = random.randint(1, 50)
    time.sleep(3)
    if res == case:
        pot += mise * 2
        print(res, " - GG t tro for wallah")

    elif case % 2 == res % 2:
        print(res, " - pas ouf mais t rembourser")
    else:
        pot -= mise
        print(res," - reesaye bg")
        
    print("Il te reste ", pot,"€")
    time.sleep(3)
print("plus d'argent, va retirer stp")






