import time


def pompe(ls,etat):
    while True:
        activation_signal = ls.inp(("activation_pompe", str))
        if activation_signal:
            etat = "activée"
            print("Pompe activée\n")

        deactivation_signal = ls.inp(("desactivation_pompe", str))
        if deactivation_signal:
            etat = "désactivée"
            print("Pompe désactivée\n")

        time.sleep(2)

def ventilateur(ls, etat):
    while True:
        activation_signal = ls.inp(("activation_ventilateur", str))
        if activation_signal:
            etat = "activée"
            print("Ventilateur activé\n")

        deactivation_signal = ls.inp(("desactivation_ventilateur", str))
        if deactivation_signal:
            etat = "désactivée"
            print("Ventilateur désactivé\n")

        time.sleep(2)

def agentCommandePompeVentilateur(ls,seuil_CH4,seuil_CO):
    while True:
        ls.inp(("detection_H2O_haut",str))
        y = ls.rd(("niveau_CH4", str, None , float))
        z = ls.rd(("niveau_CO", str, None , float))
        if(len(y) > 0) and (len(z) > 0):
            y = y[0][2]
            z = z[0][2]

            if(y < seuil_CH4 and z < seuil_CO):
                print("Le niveau de gaz est bas, activation de la pompe\n")
                ls.out(("activation_pompe", str))
                ls.out(("detection_H2O_bas",str))
                ls.out(("detection_gaz_haut",str))
            else:
                print("Le niveau de gaz est haut, activation du ventilateur\n")
                ls.out(("activation_ventilateur", str))
                ls.out(("detection_gaz_bas",str))
        time.sleep(2)