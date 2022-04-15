#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    total_seconde = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    # ou : return temps[3] + 60*temps[2] + 60*60*temps[1] + temps[0]*(60*60*24)
    return total_seconde

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    tmps = (seconde//86400, (seconde%86400)//3600, ((seconde%86400)%3600)//60, ((seconde%86400)%3600)%60)
    return tmps

#def secondeEnTemps(seconde):
    #temps_jour = seconde//(24*3600)
    #seconde = seconde%(24*3600)

    #temps_heure = seconde//3600
    #seconde = seconde%60

    #temps_minute = seconde//60
    #temps_seconde = seconde%60
    
    #return (int(tems_jour), int(temps_heure, int(temps_minute), int(temps_seconde)))

temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

print("Exo 3")
#def afficheTemps(temps):
#    str_temps = ''
#    if temps[0] > 1 :
#        str_temps += f'{temps[0]} jours'
#    elif temps[0]> 0 :
#        str_temps += f'{temps[1]} jour'
#    if temps[0]>0 and temps[1] > 0 or temps[2]>0 or temps[3]>0:
#        str_temps += ", "
#    
#    if temps[1] > 1 :
#        str_temps += f'{temps[1]} heures'
#    elif temps[1]>0 :
#        str_temps += f'{temps[1]} heure'
#    if temps[1]>0 and temps[2] > 0 or temps[3]>0:
#        str_temps += ", "
#    
#    if temps[2] > 1 :
#        str_temps += f'{temps[2]} minutes'
#    elif temps[2]>0 :
#        str_temps += f'{temps[2]} minute'
#    if temps[2]>0 and temps[3] > 0:
#        str_temps += ", "
#    
#    if temps[3] > 1 :
#        str_temps += f'{temps[3]} secondes'
#    elif temps[3]>0  :
#        str_temps += f'{temps[1]} seconde'
#
#    print(str_temps)

def afficheTemps(temps):
    if temps[0] != 0 and temps[0] > 1:
        print(temps[0], "jours", end=" ")
    elif temps[0] == 1:
        print(temps[0], "jour", end=" ")
    if temps[1] != 0 and temps[1] > 1:
        print(temps[1], "heures", end=" ")
    elif temps[1] == 1:
        print(temps[1], "heure", end=" ")
    if temps[2] != 0 and temps[2] > 1:
        print(temps[2], "minutes", end=" ")
    elif temps[2] == 1:
        print(temps[2], "minute", end=" ")
    if temps[3] != 0 and temps[3] > 1:
        print(temps[3], "secondes", end=" ")
    elif temps[3] == 1:
        print(temps[3], "seconde", end=" ")

print(afficheTemps((1,0,14,23)))


def demandeTemps():
    jour = int(input("donner un nombre de jour"))
    while jour < 0 :
        jour = int(input("donner un nombre de jours"))
    heure = int(input("donner"))
    

def sommeTemps(temps1,temps2):
    jours = temps1[0] + temps2[0]
    heures = temps1[1] + temps2[1]
    minutes = temps1[2]+temps2[2]
    secondes = temps1[3]+temps2[3]
    if secondes > 60 :
        minutes += secondes%60
    if minutes > 60:
        heures += minutes%60
    if heures > 24 :
        jours += heures%24
    
    print(jours, heures, minutes, secondes)
        

sommeTemps((2,3,4,25),(5,22,57,1))

def sommeTemps(temps1, temps2):
    seconde_t1 = tempsEnSeconde(temps1)
    seconde_t2 = tempsEnSeconde(temps2)
    return secondeEnTemps(seconde_t1 + seconde_t2)

def proportions(temps, proportion):
    seconde_t = tempsEnSeconde(temps)

    return secondeEnTemps(seconde_t*proportion)


def tempsEnDate(temps):
    

def afficheDate(date = -1):
    pass
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()