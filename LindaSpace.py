import threading
import queue

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

# Agent capteur H20
def agentCapteurH20():
    niveau_H2O = None
    print("Agent capteur H20")
    ls.out(("niveau_H2O",str, niveau_H2O, type(niveau_H2O)))
    print("Tuplespace:", ls)
    # agentCapteurH20()

def agentCapteurCH4():
    niveau_CH4 = None
    print("Agent capteur CH4")
    ls.out(("niveau_CH4",str, niveau_CH4, type(niveau_CH4)))
    print("Tuplespace:", ls)
    # agentCapteurCH4()

def agentCapteurCO():
    niveau_CO = None
    print("Agent capteur CO")
    ls.out(("niveau_CO2",str, niveau_CO, type(niveau_CO)))
    print("Tuplespace:", ls)
    # agentCapteurCO2()

def pompe(etat):
    if(etat == "on"):
        ls.inp(("activation_pompe", str))
        print("Pompe activée")
    else:
        ls.inp(("desactivation_pompe", str))
        print("Pompe désactivée")

def ventilateur(etat):
    if(etat == "on"):
        ls.inp(("activation_ventilateur", str))
        print("Ventilateur activé")
    else:
        ls.inp(("desactivation_ventilateur", str))
        print("Ventilateur désactivé")
    
def agentH2O_haut(seuil_haut):
    ls.rd(("détection_H2O_haut", str))
    x = ls.rd(("niveau_H2O", str, "valeur_H2O" , float))[0][3]
    if(x > seuil_haut):
        ls.out(("H2O_detect",str))
        ls.inp(("détection_H2O_haut", str))
        # agentH2O_haut(seuil_haut)
    else:
        # agentH2O_haut(seuil_haut)
        pass



# Exemple d'utilisation
if __name__ == "__main__":
    ls = LindaSpace()
    agentCapteurH20()
    agentCapteurCH4()
    agentCapteurCO()

    # # Ajouter des tuples
    # ls.out(())
    # ls.out((2, 'orange'))
    # ls.out((1, 'banana'))

    # # Afficher l'état actuel de l'espace de tuples
    # print("Tuplespace:", ls)

    # # Lire un tuple correspondant au modèle
    # template = (1, None)
    # result = ls.inp(template)
    # print("Read Tuple:", result)

    # # Afficher l'état mis à jour de l'espace de tuples
    # print("Tuplespace:", ls)
    print("LindaSpace")


