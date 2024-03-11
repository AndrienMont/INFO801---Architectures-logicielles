import threading
import queue
import time
import random


SEUIL_H2O_HAUT = 4.0
SEUIL_H2O_BAS = 2.0
SEUIL_CH4 = 0.5
SEUIL_CO = 0.5

niveau_H2O = 5.0
niveau_CH4 = 0.3
niveau_CO = 0.3

class LindaSpace:
    def __init__(self):
        self.tuplespace = queue.Queue()
        self.lock = threading.Lock()

    def out(self, tuple_data):
        with self.lock:
            self.tuplespace.put(tuple_data)

    def inp(self, template):
        with self.lock:
            matching_tuples = [t for t in list(self.tuplespace.queue) if self.match(template, t)]
            if matching_tuples:
                selected_tuple = matching_tuples[0]
                self.tuplespace.queue.remove(selected_tuple)
                return selected_tuple
            else:
                return None

    def rd(self, template):
        with self.lock:
            matching_tuples = [t for t in list(self.tuplespace.queue) if self.match(template, t)]
            return matching_tuples

    def match(self, template, tuple_data):
        if len(template) != len(tuple_data):
            return False

        for t, d in zip(template, tuple_data):
            if t is not None and t != d:
                return False

        return True

    def __str__(self):
        with self.lock:
            return str(list(self.tuplespace.queue))

# Agent capteur H2O
def agentCapteurH2O(ls):
    niveau_H2O = random.uniform(1.0, 5.0)
    print("Agent capteur H2O\n")
    print(str(niveau_H2O)+"\n")
    ls.inp(("niveau_H2O",str, None, type(niveau_H2O)))
    ls.out(("niveau_H2O",str, niveau_H2O, type(niveau_H2O)))
    # print("Tuplespace:", ls)
    time.sleep(2)
    agentCapteurH2O(ls)

# Agent capteur CH4
def agentCapteurCH4(ls):
    niveau_CH4 = random.uniform(0.1, 0.9)
    print("Agent capteur CH4\n")
    ls.inp(("niveau_CH4",str, None, type(niveau_CH4)))
    ls.out(("niveau_CH4",str, niveau_CH4, type(niveau_CH4)))
    # print("Tuplespace:", ls)
    time.sleep(3)
    agentCapteurCH4(ls)

# Agent capteur CO
def agentCapteurCO(ls):
    niveau_CO = random.uniform(0.1, 0.9)
    print("Agent capteur CO\n")
    ls.inp(("niveau_CO2",str, None, type(niveau_CO)))
    ls.out(("niveau_CO2",str, niveau_CO, type(niveau_CO)))
    # print("Tuplespace:", ls)
    time.sleep(3)
    agentCapteurCO(ls)

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
    
def agentH2O_haut(ls,seuil_haut):
    h2o_haut = ls.rd(("detection_H2O_haut", str))
    if(len(h2o_haut) > 0):
        x = ls.rd(("niveau_H2O", str, None , float))
        if(len(x) > 0):
            x = x[0][2]
        # print("Niveau H2O: ", x)
        # print("\n")
        if(x > seuil_haut):
            ls.out(("H2O_detect",str))
            ls.inp(("detection_H2O_haut", str))
            agentH2O_haut(ls,seuil_haut)
        else:
            agentH2O_haut(ls,seuil_haut)

def agentCommandePompeVentilateur(ls,seuil_CH4,seuil_CO):
    while True:
        ls.inp(("detection_H2O_haut",str))
        y = ls.rd(("niveau_CH4", str, None , float))
        if(len(y) > 0):
            y = y[0][2]
        z = ls.rd(("niveau_CO", str, None , float))
        if(len(z) > 0):
            z = z[0][2]
        if(y < seuil_CH4 and z < seuil_CO):
            ls.out(("activation_pompe", str))
            ls.out(("detection_H2O_bas",str))
            ls.out(("detection_gaz_haut",str))
        else:
            ls.out(("activation_ventilateur", str))
            ls.out(("detection_gaz_bas",str))

def agentGazBas(ls,seuil_CH4, seuil_CO):
    gazBas = ls.rd(("detection_gaz_bas",str))
    if(len(gazBas) > 0):
        y = ls.rd(("niveau_CH4", str, None , float))
        if(len(y) > 0):
            y = y[0][2]
        z = ls.rd(("niveau_CO", str, None , float))
        if(len(z) > 0):
            z = z[0][2]
        print("\nNiveau CH4: ", y)
        print("\nNiveau CO: ", z)
        if(y < seuil_CH4 and z < seuil_CO):
            ls.out(("activation_pompe",str))
            ls.out(("detection_H2O",str))
            ls.inp(("detection_gaz_bas",str))
            agentGazBas(ls,seuil_CH4, seuil_CO)
        else:
            agentGazBas(ls,seuil_CH4, seuil_CO)

def agentSurveillanceGazHaut(ls,seuil_CH4, seuil_CO):
    while True:
        gazHaut = ls.rd(("detection_gaz_haut",str))
        if(len(gazHaut) > 0):
            y = ls.rd(("niveau_CH4", str, None , float))
            if(len(y) > 0):
                y = y[0][2]
            z = ls.rd(("niveau_CO", str, None , float))
            if(len(z) > 0):
                z = z[0][2]
            print("\nNiveau CH4: ", y)
            print("\nNiveau CO: ", z)
            if(y < seuil_CH4 and z < seuil_CO):
                ls.out(("desactivation_ventilateur",str))
                ls.out(("detection_H2O",str))
                ls.inp(("detection_gaz_haut",str))
            time.sleep(2)

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
                ls.out(("desactivation_pompe",str))
                ls.out(("desactivation_ventilateur",str))
                ls.inp(("detection_H2O_bas",str))
                ls.inp(("detection_gaz_haut",str))
                ls.out(("detection_H2O_haut",str))
            else:
                ls.out(("activation_pompe",str))

# Exemple d'utilisation
if __name__ == "__main__":
    ls = LindaSpace()

    # Définition des niveau pour débuter le système
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
    surveillance_gaz_haut_thread = threading.Thread(target=agentSurveillanceGazHaut, args=(ls, SEUIL_CH4, SEUIL_CO))
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
