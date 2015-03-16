from game import Agent
import foodHelp

class MinimaxAgent(Agent):
  def getAction(self, gameState, agent):
    print "minimax!"
    bestAction = "Stop"
    bestVal = -999
    nextAgent = agent + 1
    depth = 10
    # iterate through possible actions, keep track of the one with the highest value
    for action in gameState.getLegalActions(agent):
      print action
      if action != "Stop":
        val = self.min(depth - 1, nextAgent, gameState.generateSuccessor(agent, action))
        if val > bestVal:
          bestVal = val
          bestAction = action
          
    return bestAction	
	
  def max (self, depth, agent, gameState):
    print "max at depth", depth
    # evaluate the current state if the game has ended or if the predetermined depth has been reached
    if depth <= 0 or gameState.isOver():
      return self.evaluationFunction(gameState)
    bestVal = -9999
    #
    if (agent + 1) == gameState.getNumAgents():
      for action in gameState.getLegalActions(agent):
        if action != "Stop":
          val = self.min(depth - 1, 0, gameState.generateSuccessor(agent, action))
          if val < bestVal:
            bestVal = val
    else: 
      for action in gameState.getLegalActions(agent):
        if action != "Stop":
          val = self.min(depth, agent + 1, gameState.generateSuccessor(agent, action))
          if val > bestVal:
            bestVal = val
            
    return bestVal

  def min (self, depth, agent, gameState):
    print "min at depth", depth
    # evaluate the current state if the game has ended or if the predetermined depth has been reached
    if depth <= 0 or gameState.isOver():
      return self.evaluationFunction(gameState)
    bestVal = 9999
    if (agent + 1) == gameState.getNumAgents():
      for action in gameState.getLegalActions(agent):
        if action != "Stop":
          val = self.max(depth - 1, 0, gameState.generateSuccessor(agent, action))
          if val < bestVal:
            bestVal = val
    else:
      print gameState.getLegalActions(agent)
      for action in gameState.getLegalActions(agent):
        if action != "Stop":
          val = self.max(depth, agent + 1, gameState.generateSuccessor(agent, action))
          if val < bestVal:
            bestVal = val
            
    return bestVal
	
  def evaluationFunction(self, gameState, agent):
    val = 0
    if gameState.isOver():
      if len(foodHelp.getMyFoodList()) > len(foodHelp.getEnemyFoodList()):
        val += 1000
      else:
        val -= 1000
    val -=  (20 - len(foodHelp.getEnemyFoodList())) * 5
    val +=  gameState.getScore() * 5
    
    return val
	  