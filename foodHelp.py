from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game

def getMyFoodList(dummyAgent,gameState):
  # Getting our food and getting indicies of each of our food's location
  myFoodList = []
  dummyAgent.myFood = dummyAgent.getFoodYouAreDefending(gameState)
  xCounter = 0
  yCounter = 0
  for x in dummyAgent.myFood:
    for y in x:
      if True == y:
        myFoodList.append((xCounter,yCounter))
      yCounter += 1
    xCounter += 1
    yCounter = 0
  return myFoodList

def getEnemyFoodList(dummyAgent,gameState):
  # Getting enemy fod and getting indicies of each of their food's location
  enemyFoodList = []
  dummyAgent.enemyFood = dummyAgent.getFood(gameState)
  xCounter = 0
  yCounter = 0
  for x in dummyAgent.enemyFood:
    for y in x:
      if True == y:
        enemyFoodList.append((xCounter,yCounter))
      yCounter += 1
    xCounter += 1
    yCounter = 0
  return enemyFoodList

def getClosestFoodPosition(dummyAgent,gameState,agentIndex):
  # Gets the position of the food closest to this agent.
  bestDistance = 999999999999
  foodPos = (0,0)
  enemyFoodList = getEnemyFoodList(dummyAgent,gameState)
  for pos in enemyFoodList:
    distance = dummyAgent.getMazeDistance(pos,gameState.getAgentPosition(agentIndex))
    if distance < bestDistance:
      bestDistance = distance
      foodPos = pos
  return foodPos

def getClosestAgent(dummyAgent,position,gameState,agentList):
  # Returns the agent closest to a specific position.
  bestDistance = 99999999999
  bestAgent = "None"
  for theAgent in agentList:
    print theAgent
    print position
    print gameState.getAgentPosition(theAgent)
    distance = dummyAgent.getMazeDistance(position,gameState.getAgentPosition(theAgent))
    if distance < bestDistance:
      bestDistance = distance
      bestAgent = theAgent
  return bestAgent

def getClosestEnemyCapsulePosition(dummyAgent,gameState,agentIndex):
  # Gets the position of the closest enemy pellet to the agent.
  bestDistance = 99999999999
  capsulePos = (0,0)
  capsuleList = dummyAgent.getCapsules(gameState)
  if capsuleList == []:
    return "None"
  for pos in capsuleList:
    distance = dummyAgent.getMazeDistance(pos,gameState.getAgentPosition(agentIndex))
    if distance < bestDistance:
      bestDistance = distance
      capsulePos = pos
  return capsulePos

def getClosestTeamCapsulePosition(dummyAgent,gameState,agentIndex):
  # Gets the position of the closest of our pellet to the agent.
  bestDistance = 99999999999
  capsulePos = (0,0)
  capsuleList = dummyAgent.getCapsulesYouAreDefending(gameState)
  if capsuleList == []:
    return "None"
  for pos in capsuleList:
    distance = dummyAgent.getMazeDistance(pos,gameState.getAgentPosition(agentIndex))
    if distance < bestDistance:
      bestDistance = distance
      capsulePos = pos
  return capsulePos


  # TODO:
  # Finding power pellet,  
