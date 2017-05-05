from Game import *
from Neuron import *
from Player import *
import time

une_partie = Game(15)
Guettouche = HumanPlayer("Guettouche Islam")
Machine = CPUPlayer("Machine","easy",15)

une_partie.start(Guettouche,Machine,True)
time.sleep( 3 )