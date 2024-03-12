import threading
from LindaSpace import LindaSpace
from agentCapteur import agentCapteurCH4, agentCapteurCO, agentCapteurH2O
from agentMachine import agentCommandePompeVentilateur, pompe, ventilateur
from agentSeuil import agentGazBas, agentGazHaut, agentH2O_bas, agentH2O_haut

SEUIL_H2O_HAUT = 4.0
SEUIL_H2O_BAS = 2.0
SEUIL_CH4 = 0.5
SEUIL_CO = 0.5

niveau_H2O = 5.0
niveau_CH4 = 0.3
niveau_CO = 0.3


# Exemple d'utilisation
if __name__ == "__main__":
    ls = LindaSpace()

    # Définition des niveau pour débuter le système
    print("Démarrage du système minier\n\n")
    print("Seuil H2O haut: ", SEUIL_H2O_HAUT)
    print("\nSeuil H2O bas: ", SEUIL_H2O_BAS)
    print("\nSeuil CH4: ", SEUIL_CH4)
    print("\nSeuil CO: ", SEUIL_CO)
    print("\n")
    ls.out(("niveau_H2O", str, niveau_H2O, type(niveau_H2O)))
    ls.out(("niveau_CH4", str, niveau_CH4, type(niveau_CH4)))
    ls.out(("niveau_CO", str, niveau_CO, type(niveau_CO)))

    # ls.out(("activation_pompe", str))
    # print("Tuplespace:", ls)
    # print("rd:", ls.rd(("activation_pompe", str)))
    # print("inp:", ls.inp(("activation_pompe", str)))
    # print("Tuplespace:", ls)
    
    capteur_h2o_thread = threading.Thread(target=agentCapteurH2O, args=(ls,))
    capteur_ch4_thread = threading.Thread(target=agentCapteurCH4, args=(ls,))
    capteur_co_thread = threading.Thread(target=agentCapteurCO, args=(ls,))
    h2o_haut_thread = threading.Thread(target=agentH2O_haut, args=(ls, SEUIL_H2O_HAUT))
    gaz_bas_thread = threading.Thread(target=agentGazBas, args=(ls, SEUIL_CH4, SEUIL_CO))
    surveillance_gaz_haut_thread = threading.Thread(target=agentGazHaut, args=(ls, SEUIL_CH4, SEUIL_CO))
    h2o_bas_thread = threading.Thread(target=agentH2O_bas, args=(ls, SEUIL_H2O_BAS))
    ventilateur_thread = threading.Thread(target=ventilateur, args=(ls,"off"))
    pompe_thread = threading.Thread(target=pompe, args=(ls,"off"))
    commande_thread = threading.Thread(target=agentCommandePompeVentilateur, args=(ls, SEUIL_CH4, SEUIL_CO))

    capteur_h2o_thread.start()
    capteur_ch4_thread.start()
    capteur_co_thread.start()
    h2o_haut_thread.start()
    gaz_bas_thread.start()
    surveillance_gaz_haut_thread.start()
    h2o_bas_thread.start()
    ventilateur_thread.start()
    pompe_thread.start()
    commande_thread.start()

    capteur_h2o_thread.join()
    capteur_ch4_thread.join()
    capteur_co_thread.join()
    h2o_haut_thread.join()
    gaz_bas_thread.join()
    surveillance_gaz_haut_thread.join()
    h2o_bas_thread.join()
    ventilateur_thread.join()
    pompe_thread.join()
    commande_thread.join() 
