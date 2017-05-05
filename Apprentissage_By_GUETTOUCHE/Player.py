import random
from Neuron import *

class Player:
    def __init__(self,name):
        self.name = name
        self.nbWin = 0
    def getName(self):
        return self.name
    def getNbWin(self):
        return self.nbWin
    def addWin(self):
        self.nbWin+=1
    def addLoss(self):
        pass

class HumanPlayer(Player):
    def play(self,sticks):
        if sticks==1: return 1
        else:
            correct = False
            while not correct:
                nb = input('Sticks?\n')
                try:
                    nb=int(nb)
                    if nb>=1 and nb<=3 and sticks-nb>=0:
                        correct=True
                        print("\n")
                except: pass
            return nb

class CPUPlayer(Player):
    def __init__(self,name,mode,nbSticks):
        super().__init__(name)
        self.mode = mode
        self.netw = NeuronNetwork(3,nbSticks)
        self.previousNeuron = None
        self.nbErreur = 0
        self.nbTour = 0
    def play(self,sticks):
        if self.mode=='easy': return self.playEasy(sticks)
        elif self.mode=='hard': return self.playHard(sticks)
        else: return self.playMedium(sticks)

#MODIFIER		
    def playMedium(self,sticks):
        if sticks > 4: 
            return random.randint(1,3) 
        elif sticks == 1:
            return 1
        else:
            return sticks - 1
		
    def playEasy(self,sticks):
        return self.playRandom(sticks)
    def playRandom(self,sticks):
        if sticks<4: return random.randint(1,sticks)
        else: return random.randint(1,3)
		
#MODIFIER
    def playHard(self,sticks):
	# TODO utiliser le réseau neuronal pour choisir le nombre de bâtons à jouer
        # utiliser l'attribut self.previousNeuron pour avoir le neuron précédemment sollicité dans la partie
        # calculer un 'shift' qui correspond à la différence entre la valeur du précédent neurone et le nombre de bâtons encore en jeu
        # utiliser la méthode 'chooseConnectedNeuron' du self.previousNeuron puis retourner le nombre de bâtons à jouer
        # bien activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible
        # attention à gérer les cas particuliers (premier tour ou sticks==1)
		
		#si cest le premier tour (self.previousNeuron retourne None)
        if self.previousNeuron==None:  
		# en recupere neurons[sticks-1]		
            self.previousNeuron = self.netw.getNeuron(sticks)
            neuron_previous = self.previousNeuron
		#on fais appel a la methode chooseConnectedNeuron afin de choisir le nombre de bâtons à jouer
            after_use_of_chooseConnectedNeuron = neuron_previous.chooseConnectedNeuron(0)
            self.previousNeuron = after_use_of_chooseConnectedNeuron
		#activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible (after_use_of_chooseConnectedNeuron) 
		#self.path[neuron_previous]=after_use_of_chooseConnectedNeuron
            self.netw.activateNeuronPath(neuron_previous,after_use_of_chooseConnectedNeuron)
        # Taux erreur
            if(after_use_of_chooseConnectedNeuron.index%4!=1 and neuron_previous.index%4!=1):
                self.nbErreur = self.nbErreur+1
            self.nbTour = self.nbTour+1
            return (neuron_previous.index-after_use_of_chooseConnectedNeuron.index)
			
		#si cest le dernier tour sticks==1 incrementer le nombre de tour et retourner 1
        elif sticks==1:                                             
            self.nbTour = self.nbTour+1
            return 1 
			
		#si self.previousNeuron != None et sticks!=1	alors
        else: 
		#on recupere le neuron précédemment sollicité dans la partie		
            neuron_previous = self.previousNeuron
		#on fais appel a la methode chooseConnectedNeuron afin de choisir le nombre de bâtons à jouer
            after_use_of_chooseConnectedNeuron = neuron_previous.chooseConnectedNeuron(neuron_previous.index-sticks)
            self.previousNeuron = after_use_of_chooseConnectedNeuron
		#activer le réseau de neurones avec la méthode 'activateNeuronPath' après avoir choisi un neurone cible (after_use_of_chooseConnectedNeuron) 
		#self.path[neuron_previous]=after_use_of_chooseConnectedNeuron
            self.netw.activateNeuronPath(neuron_previous,after_use_of_chooseConnectedNeuron)
        # Taux erreur
            if(after_use_of_chooseConnectedNeuron.index%4!=1 and sticks%4!=1):
                self.nbErreur = self.nbErreur+1
            self.nbTour = self.nbTour+1
            return sticks-after_use_of_chooseConnectedNeuron.index
			
    def getNeuronNetwork(self): return self.netw
    def setNeuronNetwork(self,ns): self.netw = ns
    def getTauxErreur(self): return int((self.nbErreur/self.nbTour)*100)
    def resetTauxErreur(self): 
        self.nbErreur = 0
        self.nbTour = 0
    def addWin(self):
        super().addWin()
        self.netw.recompenseConnections()
        self.previousNeuron=None
    def addLoss(self):
        super().addLoss()
        self.previousNeuron=None




        


