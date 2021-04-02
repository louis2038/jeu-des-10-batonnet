
from algorytm import IA

commence = True

player = IA(10)

print("bienvenue au jeux des 10 baton !")
print("voici les regles:")
print("chaqu'un son tour, vous devez prendre 1 , 2 ou 3 baton (minimum 1 baton), le joueur qui a pris le dernier baton a perdu !")


def qui_commence(commence):
    if commence == True:
        return False
    else:
        return True


def nouveau_jeu(commence):
    player.nbs_baton = 10
    commence = qui_commence(commence)
    if commence == False:
        print("")
        print("------------")
        print("")
        print("nouveaux jeu ! ")
       
    else:
  
        print("")
        print("------------")
        print("")
        print("nouveaux jeux")
        print("il reste {} baton".format(player.nbs_baton))
        rep = player.reponse()
        rep = int(rep)
        player.nbs_baton = player.nbs_baton - rep
        print("tour de l'IA, il reste {} baton".format(player.nbs_baton))
    return commence


def votre_tour(commence):
    print("")
    if player.nbs_baton < 1:
        print("vous avez GAGNE !")
        return True

    print("c'est votre tour: il y a {} baton".format(player.nbs_baton))
    choix_baton_retirer = input("combien de baton voulez-vous retirer ? -->")
    try:
        choix_baton_retirer = int(choix_baton_retirer)
    except:
        print("erreur -> entrer un chifre !")
        return False

    if (choix_baton_retirer == 1) or (choix_baton_retirer == 2) or (choix_baton_retirer == 3):
        if (player.nbs_baton - choix_baton_retirer) < 1:
            print("vous avez PERDU !")
            return True

        player.nbs_baton = player.nbs_baton - choix_baton_retirer
        print("il reste {} baton".format(player.nbs_baton))
        rep = player.reponse()
        rep = int(rep)
        player.nbs_baton = player.nbs_baton - rep
        print("tour de l'IA, il reste {} baton".format(player.nbs_baton))
    else:
        print("valeur incorect ! (vous pouvez prendre 1 , 2 ou 3 baton)")
        return False




fin_tour = False
statut = True
while fin_tour == False:
    if(statut == True):
        commence = nouveau_jeu(commence)
    statut = votre_tour(commence)


