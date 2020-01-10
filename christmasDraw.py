# Automated draw of christmas gifts among 7 individuals

import random

# Initial setup of Variables

# Buyers
buyer1 = "Madeleine"
buyer2 = "Fredrik"
buyer3 = "Hanna-Maria"
buyer4 = "Ante"
buyer5 = "Anne"
buyer6 = "Mats"
buyer7 = "Hakan"

# Who corresponding buyer had 2019, cannot be same in 2020
prev1 = "Mats"
prev2 = "Ante"
prev3 = "Hakan"
prev4 = "Hanna-Maria"
prev5 = "Madeleine"
prev6 = "Anne"
prev7 = "Fredrik"

# Placeholders for 2020
get1 = ""
get2 = ""
get3 = ""
get4 = ""
get5 = ""
get6 = ""
get7 = ""

buyList = [buyer1, buyer2, buyer3, buyer4, buyer5, buyer6, buyer7]
buyTotal = 0

# Contineously make each valid before continue, loop until all 7 are set

while buyTotal < 7: 
    if buyTotal == 0:
        get1 = random.choice(buyList)
        if get1 != buyer1 and get1 != prev1:
            buyList.remove(get1)
            buyTotal = 1

    if buyTotal == 1:
        get2 = random.choice(buyList)
        if get2 != buyer2 and get2 != prev2:
            buyList.remove(get2)
            buyTotal = 2

    if buyTotal == 2:
        get3 = random.choice(buyList)
        if get3 != buyer3 and get3 != prev3:
            buyList.remove(get3)
            buyTotal = 3

    if buyTotal == 3:
        get4 = random.choice(buyList)
        if get4 != buyer4 and get4 != prev4:
            buyList.remove(get4)
            buyTotal = 4

    if buyTotal == 4:
        get5 = random.choice(buyList)
        if get5 != buyer5 and get5 != prev5:
            buyList.remove(get5)
            buyTotal = 5

    if buyTotal == 5:
        get6 = random.choice(buyList)
        if buyer6 in buyList and buyer5 in buyList:
            get1 = ""
            get2 = ""
            get3 = ""
            get4 = ""
            get5 = ""
            get6 = ""
            get7 = ""
            buyList = [buyer1, buyer2, buyer3, buyer4, buyer5, buyer6, buyer7]
            buyTotal = 0

        elif get6 != buyer6 and get6 != prev6:
            buyList.remove(get6)
            buyTotal = 6

    if buyTotal == 6:
        get7 = random.choice(buyList)
        if buyer7 in buyList or buyer2 in buyList:
            get1 = ""
            get2 = ""
            get3 = ""
            get4 = ""
            get5 = ""
            get6 = ""
            get7 = ""
            buyList = [buyer1, buyer2, buyer3, buyer4, buyer5, buyer6, buyer7]
            buyTotal = 0

        elif get7 != buyer7 and get7 != prev7:
            buyList.remove(get7)
            buyTotal = 7


print ("{}: {}".format(buyer1, get1))
print ("{}: {}".format(buyer2, get2))
print ("{}: {}".format(buyer3, get3))
print ("{}: {}".format(buyer4, get4))
print ("{}: {}".format(buyer5, get5))
print ("{}: {}".format(buyer6, get6))
print ("{}: {}".format(buyer7, get7))
