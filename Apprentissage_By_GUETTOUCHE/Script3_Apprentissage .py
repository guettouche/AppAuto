from Game import *
from Neuron import *
from Player import *
import pickle
import time

NB_PARTIES = 5000

une_partie = Game(15)


# ----------- Machine1 en mode EASY VS Machine2 en mode EASY -----------
Machine1 = CPUPlayer("La Machine 1 Easy","easy",15)
Machine2 = CPUPlayer("La Machine 2 Easy","easy",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")


# ----------- Machine1 en mode EASY VS Machine2 en mode MEDIUM -----------
Machine1 = CPUPlayer("La Machine 1 Easy","easy",15)
Machine2 = CPUPlayer("La Machine 2 Medium","medium",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- Machine1 en mode EASY VS Machine2 en mode HARD -----------
Machine1 = CPUPlayer("La Machine 1 Easy","easy",15)
Machine2 = CPUPlayer("La Machine 2 Hard","hard",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")


# ----------- Machine1 en mode MEDIUM VS Machine2 en mode EASY -----------
Machine1 = CPUPlayer("La Machine 1 Medium","medium",15)
Machine2 = CPUPlayer("La Machine 2 Easy","easy",15)


for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")



# ----------- Machine1 en mode MEDIUM VS Machine2 en mode MEDIUM -----------
Machine1 = CPUPlayer("La Machine 1 Medium","medium",15)
Machine2 = CPUPlayer("La Machine 2 Medium","medium",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")


# ----------- Machine1 en mode MEDIUM VS Machine2 en mode HARD -----------
Machine1 = CPUPlayer("La Machine 1 Medium","medium",15)
Machine2 = CPUPlayer("La Machine 2 Hard","hard",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")




# -----------   Machine1 en mode HARD VS Machine2 en mode EASY -----------
Machine1 = CPUPlayer("La Machine 1 Hard","hard",15)
Machine2 = CPUPlayer("La Machine 2 Easy","easy",15)


for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# -----------  Machine1 en mode HARD VS Machine2 en mode MEDIUM -----------
Machine1 = CPUPlayer("La Machine 1 Hard","hard",15)
Machine2 = CPUPlayer("La Machine 2 Medium","medium",15)


for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

# ----------- Machine1 en mode HARD VS Machine2 en mode HARD -----------
Machine1 = CPUPlayer("La Machine 1 Hard","hard",15)
Machine2 = CPUPlayer("La Machine 2 Hard","hard",15)

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")



if (Machine1.getNbWin()>Machine2.getNbWin()):
	neurons = Machine1.getNeuronNetwork()
else:
	neurons = Machine2.getNeuronNetwork()

# Phase d’apprentissage : l'enregistrement du réseau neuronal dans un ﬁchier sérialisé
with open('neuronNetwork_By_Guettouche.nnw','wb') as output: pickle.dump(neurons,output,pickle.HIGHEST_PROTOCOL)
time.sleep( 5 )


