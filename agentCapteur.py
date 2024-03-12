# Agent capteur H2O
import random
import time


def agentCapteurH2O(ls):
    niveau_H2O = random.uniform(1.0, 5.0)
    print("Agent capteur H2O actif\n")
    # print(str(niveau_H2O)+"\n")
    ls.inp(("niveau_H2O",str, None, type(niveau_H2O)))
    ls.out(("niveau_H2O",str, niveau_H2O, type(niveau_H2O)))
    # print("Tuplespace:", ls)
    time.sleep(2)
    agentCapteurH2O(ls)

# Agent capteur CH4
def agentCapteurCH4(ls):
    niveau_CH4 = random.uniform(0.1, 0.9)
    print("Agent capteur CH4 actif\n")
    ls.inp(("niveau_CH4",str, None, type(niveau_CH4)))
    ls.out(("niveau_CH4",str, niveau_CH4, type(niveau_CH4)))
    # print("Tuplespace:", ls)
    time.sleep(3)
    agentCapteurCH4(ls)

# Agent capteur CO
def agentCapteurCO(ls):
    niveau_CO = random.uniform(0.1, 0.9)
    print("Agent capteur CO actif\n")
    ls.inp(("niveau_CO2",str, None, type(niveau_CO)))
    ls.out(("niveau_CO2",str, niveau_CO, type(niveau_CO)))
    # print("Tuplespace:", ls)
    time.sleep(3)
    agentCapteurCO(ls)