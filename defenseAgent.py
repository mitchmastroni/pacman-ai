import util
import random
import game
import capture

class InferenceModule:
  """
  An inference module tracks a belief distribution over a ghost's location.
  This is an abstract class, which you should not modify.
  """
  
  ############################################
  # Useful methods for all inference modules #
  ############################################
  
  def __init__(self, enemyIndex):
    "Sets the ghost agent for later access"
    self.index = enemyIndex
    
  def getPositionDistribution(self, gameState):
    """
    Returns a distribution over successor positions of the ghost from the given gameState.
    
    You must first place the ghost in the gameState, using setGhostPosition below.
    """
    ghostPosition = gameState.getAgentPosition(self.index) # The position you set
    ghostLegal = gameState.getLegalActions(self.index)
    actionDist = [(1/len(ghostLegal),action) for action in ghostLegal]
    dist = util.Counter()
    for action, prob in actionDist.items():
      successorPosition = game.Actions.getSuccessor(ghostPosition, action)
      dist[successorPosition] = prob
    return dist
  
  def setGhostPosition(self, gameState, ghostPosition):
    """
    Sets the position of the ghost for this inference module to the specified
    position in the supplied gameState.
    """
    conf = game.Configuration(ghostPosition, game.Directions.STOP)
    gameState.data.agentStates[self.index] = game.AgentState(conf, False)
    return gameState
  
  def observeState(self, gameState):
    "Collects the relevant noisy distance observation and pass it along."
    distances = gameState.getNoisyGhostDistances()
    if len(distances) >= self.index: # Check for missing observations
      obs = distances[self.index - 1]
      self.observe(obs, gameState)
      
  def initialize(self, gameState):
    "Initializes beliefs to a uniform distribution over all positions."
    # The legal positions do not include the ghost prison cells in the bottom left.
    self.legalPositions = [p for p in gameState.getWalls().asList(False) if p[1] > 1]   
    self.initializeUniformly(gameState)
    
  ######################################
  # Methods that need to be overridden #
  ######################################
  
  def initializeUniformly(self, gameState):
    "Sets the belief state to a uniform prior belief over all positions."
    pass
  
  def observe(self, observation, gameState):
    "Updates beliefs based on the given distance observation and gameState."
    pass
  
  def elapseTime(self, gameState):
    "Updates beliefs for a time step elapsing from a gameState."
    pass
    
  def getBeliefDistribution(self):
    """
    Returns the agent's current belief state, a distribution over
    ghost locations conditioned on all evidence so far.
    """
    pass

class ExactInference(InferenceModule):  
  def initializeUniformly(self, gameState):
    "Begin with a uniform distribution over ghost positions."
    self.beliefs = util.Counter()
    for p in self.legalPositions: self.beliefs[p] = 1.0
    self.beliefs.normalize()
  
  def observe(self, observation, gameState):

    noisyDistance = observation
    observationDistributions = {}
    if nosiyDistance not in observationDistributions:
      distribution = util.Counter()
    pacmanPosition = gameState.getAgentPosition(currentAgent.index)
 
    # Replace this code with a correct observation update
    allPossible = util.Counter() # Makes a new counter.
    for p in self.legalPositions: # For each position possible in the pac-man game
      trueDistance = util.manhattanDistance(p, pacmanPosition) # Get distance from the position to pacman.
      if emissionModel[trueDistance] > 0.0: # If the emission model at that spot is greater than 0
        allPossible[p] = emissionModel[trueDistance]*self.beliefs[p] # Multiply emission model times the current beliefs.
    allPossible.normalize() # Noramlize so everything adds up to 1.
        
    self.beliefs = allPossible # Set self.beliefs to the updated value
    
    
  def elapseTime(self, gameState):
    newCounter = util.Counter()
    for p in self.legalPositions: # For each legal position
      if self.beliefs[p] > 0.0: 
        newPosDist = self.getPositionDistribution(self.setGhostPosition(gameState,p)) # Get the possible positions and the distribution.
        for pos in newPosDist: # For each position:
	   newCounter[pos] += newPosDist[pos]*self.beliefs[p] # Update the beliefs based on the distribution.
    newCounter.normalize() # Normalize.
    self.beliefs = newCounter # Set the beliefs.
 
  def getBeliefDistribution(self):
    return self.beliefs


