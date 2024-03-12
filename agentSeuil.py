import time


def agentH2O_haut(ls,seuil_haut):
    h2o_haut = ls.rd(("detection_H2O_haut", str))
    if(len(h2o_haut) > 0):
        x = ls.rd(("niveau_H2O", str, None , float))
        if(len(x) > 0):
            x = x[0][2]
        # print("Niveau H2O: ", x)
        # print("\n")
            if(x > seuil_haut):
                print("Le niveau d'eau est haut\n")
                ls.out(("H2O_detect",str))
                ls.inp(("detection_H2O_haut", str))
                time.sleep(2)
                agentH2O_haut(ls,seuil_haut)
            else:
                time.sleep(2)
                agentH2O_haut(ls,seuil_haut)

def agentH2O_bas(ls,seuil_bas):
    while True:
        eau_bas = ls.rd(("detection_H2O_bas",str))
        if(len(eau_bas) > 0):
            x = ls.rd(("niveau_H2O", str, None , float))
            if(len(x) > 0):
                x = x[0][2]
            # print("Niveau H2O: ", x)
            # print("\n")
                if(x < seuil_bas):
                    print("Le niveau d'eau est bas, desactivation de la pompe et du ventilateur\n")
                    ls.out(("desactivation_pompe",str))
                    ls.out(("desactivation_ventilateur",str))
                    ls.inp(("detection_H2O_bas",str))
                    ls.inp(("detection_gaz_haut",str))
                    ls.out(("detection_H2O_haut",str))
                else:
                    ls.out(("activation_pompe",str))
        time.sleep(2)

def agentGazBas(ls,seuil_CH4, seuil_CO):
    gazBas = ls.rd(("detection_gaz_bas",str))
    if(len(gazBas) > 0):
        y = ls.rd(("niveau_CH4", str, None , float))
        if(len(y) > 0):
            y = y[0][2]
        z = ls.rd(("niveau_CO", str, None , float))
        if(len(z) > 0):
            z = z[0][2]
        # print("\nNiveau CH4: ", y)
        # print("\nNiveau CO: ", z)
        if(y < seuil_CH4 and z < seuil_CO):
            print("Le niveau de gaz est bas, activation de la pompe\n")
            ls.out(("activation_pompe",str))
            ls.out(("detection_H2O",str))
            ls.inp(("detection_gaz_bas",str))
            time.sleep(2)
            agentGazBas(ls,seuil_CH4, seuil_CO)
        else:
            time.sleep(2)
            agentGazBas(ls,seuil_CH4, seuil_CO)

def agentGazHaut(ls,seuil_CH4, seuil_CO):
    while True:
        gazHaut = ls.rd(("detection_gaz_haut",str))
        if(len(gazHaut) > 0):
            y = ls.rd(("niveau_CH4", str, None , float))
            if(len(y) > 0):
                y = y[0][2]
            z = ls.rd(("niveau_CO", str, None , float))
            if(len(z) > 0):
                z = z[0][2]
            # print("\nNiveau CH4: ", y)
            # print("\nNiveau CO: ", z)
            if(y < seuil_CH4 and z < seuil_CO):
                print("Le niveau de gaz est bas, desactivation du ventilateur\n")
                ls.out(("desactivation_ventilateur",str))
                ls.out(("detection_H2O",str))
                ls.inp(("detection_gaz_haut",str))
            time.sleep(2)