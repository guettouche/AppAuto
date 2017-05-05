from Game import *
from Neuron import *
from Player import *
import time

une_partie = Game(15)
Guettouche = HumanPlayer("Guettouche Islam")
Machine = CPUPlayer("Machine","hard",15)

une_partie.start(Machine,Guettouche,True)
time.sleep( 3 )