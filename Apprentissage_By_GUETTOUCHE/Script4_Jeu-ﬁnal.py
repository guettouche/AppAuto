from Game import *
from Neuron import *
from Player import *
import pickle
import time

NB_STICKS = 15

une_partie = Game(NB_STICKS)

# PLAYER NAME
playerName = input('Enter your name : \n')

# GAME MODE
gameMode = ""
while (gameMode!="easy") and (gameMode!="medium") and (gameMode!="hard"):
	gameMode = input('Choose a game mode (easy,medium,hard) : \n')

# PLAYER INSTANCIATION
PlayerHuman = HumanPlayer(playerName)
Machine = CPUPlayer("La Machine",gameMode,NB_STICKS)

#désérialisation à partir d’un ﬁchier neuronNetwork_By_Guettouche.nnw
if(gameMode == "hard"):
	with open('neuronNetwork_By_Guettouche.nnw', 'rb') as inp: ns = pickle.load(inp)
	Machine.setNeuronNetwork(ns)
	print("neuronNetwork_By_Guettouche.nnw A été chargé avec succès!\n")
	
premier = ""
while premier not in ['yes', 'no']:
	premier = input('Voulez-vous être le premier à jouer? (yes,no) : \n')
	if(premier == "yes"): 
		print(str(playerName) + " VS Machine en Mode : " + str(gameMode) +  ".\n")
		print(str(playerName) + " Bonne Chance!\n")
		une_partie.start(PlayerHuman,Machine,True)
		
	if(premier == "no"):
		print("Machine VS " + str(playerName) + " en Mode : "  + str(gameMode) +  ".\n")
		print(str(playerName) + " Bonne Chance!\n")
		une_partie.start(Machine,PlayerHuman,True)
 


time.sleep( 5 )
