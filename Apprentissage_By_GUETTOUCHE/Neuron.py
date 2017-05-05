import random

BASE_WEIGHT = 10
RECOMPENSE = 8

class NeuronNetwork:
    def __init__(self,maxDist,nbSticks):
        self.neurons = []
        for i in range(1,nbSticks+1):
            self.neurons.append(Neuron(self,i))
        for neuron in self.neurons:
            neuron.makeConnections(maxDist,nbSticks,BASE_WEIGHT)
        self.initPath()
    def initPath(self):
        self.path = {}
    def getNeuron(self,index):
        if index-1>=0 and index<=len(self.neurons): return self.neurons[index-1]
        else: return None
    def activateNeuronPath(self,neuron1,neuron2):
        self.path[neuron1]=neuron2
    def recompenseConnections(self):
        for neuron1,neuron2 in self.path.items():
            neuron1.recompenseConnection(neuron2)
        self.initPath()
    def printAllConnections(self):
        for neuron in self.neurons: neuron.printConnections()
    def printScores(self):
        scores = {}
        for neuron in self.neurons:
            for n,s in neuron.connections.items():
                if n not in scores: scores[n]=s
                else: scores[n] = scores[n] + s
        for neuron,score in scores.items():
            print(neuron.asString(),score)

class Neuron:
    def __init__(self,network,index):
        self.network = network
        self.index = index
        self.connections = {}
    def makeConnections(self,maxDist,nbSticks,baseWeight):
        if self.index!=nbSticks: nb=maxDist*2 +1
        else: nb=maxDist +1
        for i in range(1,nb):
            neuron = self.network.getNeuron(self.index-i)
            if neuron!=None: self.connections[neuron]=baseWeight
			
#MODIFIER	

    def chooseConnectedNeuron(self,shift):
        neuron = None
        # TODO méthode qui retourne un neurone connecté au neurone actuel en fonction du 'shift' (cf. CPUPlayer).
        # On devra utiliser la méthode self.weighted_choice pour choisir au hasard dans une liste de connexions disponibles en fonction de leurs poids
        #on utilise une var neuron_neuron_test afin de gérer la boucle while
		#on utilise une var copie_connections afin d'avoir une copie de la liste des neurones connecté
        neuron_test = False
        copie_connections = self.connections.copy()
		#tant que neuron_neuron_test == False choisir au hasard un neuron dans la liste de connexions disponibles en fonction de leurs poids
		#on Enlève de la liste l’élément situé à la position indiquée
        while neuron_test == False:
            neuron = self.weighted_choice(copie_connections)
			#on Enlève de la liste l’élément situé à la position indiquée
            copie_connections.pop(neuron)
			#on neuron_teste si la différence entre la 'self.index-shift' et la valeur du neurone actuel est comprise entre 1 et 3 inclus
            neuron_test = neuron.neuron_testNeuron(self.index-shift)
			#si cest oui on retourne le neuron
            if neuron_test == True: 
                return neuron
			#si le nombre d'éléments de la liste copie_connections est == 0 on retourne None
            if len(copie_connections) == 0:
                return None  
	
#MODIFIER	
    def neuron_testNeuron(self,inValue):
        # TODO renvoie un booléen : True si la différence entre la 'inValue' et la valeur du neurone actuel est comprise entre 1 et 3 inclus
        if inValue-self.index>=1 and inValue-self.index<=3: return True
        else: return False

#MODIFIER		
    def recompenseConnection(self,neuron):
        self.connections[neuron] = self.connections[neuron]+RECOMPENSE
        pass
		
    def printConnections(self):
        print("Connections of",self.asString()+":")
        for neuron in self.connections:
            print(neuron.asString(),self.connections[neuron])
    def asString(self):
        return "N"+str(self.index)
    def weighted_choice(self,connections):
       total = sum(w for c, w in connections.items())
       r = random.uniform(0, total)
       upto = 0
       for c, w in connections.items():
          if upto + w >= r: return c
          upto += w
        


        


