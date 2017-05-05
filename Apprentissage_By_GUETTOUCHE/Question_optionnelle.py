from Game import *
from Neuron import *
from Player import *
import time

une_partie = Game(15)
Machine1 = CPUPlayer("Machine1","hard",15)
Machine2 = CPUPlayer("Machine2","hard",15)

NB_PARTIES = 5000

for i in range(1,NB_PARTIES+1):
	une_partie.start(Machine1,Machine2,False)
	print("Partie Numero : " + str(i) + " : Taux D'Erreur(Machine1) = " + str(Machine1.getTauxErreur()) + "%  ||  Taux D'Erreur(Machine2) = " + str(Machine2.getTauxErreur()) + "%")
	Machine1.resetTauxErreur()
	Machine2.resetTauxErreur()

print(str(Machine1.getName()) + " : " + str(Machine1.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.")
print(str(Machine2.getName()) + " : " + str(Machine2.getNbWin()) + " victoires sur " + str(NB_PARTIES) + " parties.\n")

time.sleep( 20 )