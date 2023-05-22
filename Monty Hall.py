import random
from matplotlib import pyplot

def Monty_Hall(CHANGEMENT):
    PORTES_FERMEES = ["porte1", "porte2", "porte3"]
    PORTE_VOITURE = set([random.choice(PORTES_FERMEES)])
    CHOIX1_JOUEUR = set([random.choice(PORTES_FERMEES)])
    PORTES_FERMEES = set(PORTES_FERMEES)
    PORTES_CHEVRES = PORTES_FERMEES - PORTE_VOITURE
    CHOIX_PRESENTATEUR = random.choice(list(PORTES_CHEVRES - CHOIX1_JOUEUR))
    CHOIX_PRESENTATEUR = set([CHOIX_PRESENTATEUR])
    
    print("La voiture est cachée derrière la ", PORTE_VOITURE)
    print("Les chèvres sont cachées derrière les portes ", PORTES_CHEVRES)
    print("Le joueur choisi la porte", CHOIX1_JOUEUR, "\n")
    print("Le présentateur ouvre la porte ", CHOIX_PRESENTATEUR)
    print("Seules les portes ", PORTES_FERMEES-CHOIX_PRESENTATEUR, "sont fermées")

    if CHANGEMENT == 0:
        print("Le joueur ne change pas de porte \n")
        print("Le joueur ouvre la porte ", CHOIX1_JOUEUR)
        if CHOIX1_JOUEUR == PORTE_VOITURE:
            print("Le joueur a gagné \n")
            g=1
        else:
            print("le joueur à perdu \n")
            g=0
    elif CHANGEMENT == 1:
        print("Le joueur change de porte \n")
        CHOIX2_JOUEUR = PORTES_FERMEES - CHOIX1_JOUEUR -CHOIX_PRESENTATEUR
        print("le joueur ouvre la porte ", CHOIX2_JOUEUR)
        if CHOIX2_JOUEUR == PORTE_VOITURE:
            print("Le joueur a gagné \n")
            g=1
        else:
            print("Le joueur a perdu \n")
            g=0
    return(g)



def Moyenne(r, CHANGEMENT):
    TOTAL=0
    i=0
    while i<r:
        TOTAL+=Monty_Hall(CHANGEMENT)
        i+=1
    MOYENNE= TOTAL/r
    return(MOYENNE)


def Graphe(r, CHANGEMENT):
    i=1
    GRAPHE=[]
    TOTAL=Monty_Hall(CHANGEMENT)
    MOYENNE= TOTAL/i
    GRAPHE.append(MOYENNE)
    i+=1
    while i<r:
        TOTAL+=Monty_Hall(CHANGEMENT)
        MOYENNE= TOTAL/i
        GRAPHE.append(MOYENNE)
        i+=1
    pyplot.plot(GRAPHE)
    pyplot.ylim((0,1))
    return(pyplot.show())