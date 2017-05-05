import pickle
from Game import *
from Neuron import *
from Player import *
import time

une_partie = Game(15)
Machine1 = CPUPlayer("Machine1","hard",15)
Machine2 = CPUPlayer("Machine2","hard",15)

NB_PARTIES = 800

i = 0
for i in range(0, 800):
    une_partie.start(Machine1, Machine2, False)
    
print("Nombres de victoires de Machine1:")
print(str(Machine1.getNbWin()) + " / 800.\n")
print("Connections de Machine1: ")
Machine1.netw.printAllConnections()
print("")
print("Connections neuronales pondérées de Machine1: ")
Machine1.netw.printScores()
print("")
print("----------------------------------------")
print("")
print("Nombres de victoires de Machine2:")
print(str(Machine2.getNbWin()) + " / 800.\n")
print("")
print("Connections de Machine2: ")
Machine2.netw.printAllConnections()
print("")
print("Connections neuronales pondérées de Machine2: ")
Machine2.netw.printScores()

time.sleep( 20 )