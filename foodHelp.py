from captureAgents import CaptureAgent
import random, time, util
from game import Directions
import game

def getMyFoodList(agent,gameState):
  # Getting our food and getting indicies of each of our food's location
  myFoodList = []
  agent.myFood = agent.getFoodYouAreDefending(gameState)
  xCounter = 0
  yCounter = 0
  for x in agent.myFood:
    for y in x:
      if True == y:
        myFoodList.append((xCounter,yCounter))
      yCounter += 1
    xCounter += 1
    yCounter = 0
  return myFoodList

def getEnemyFoodList(agent,gameState):
  # Getting enemy fod and getting indicies of each of their food's location
  enemyFoodList = []
  agent.enemyFood = agent.getFood(gameState)
  xCounter = 0
  yCounter = 0
  for x in agent.enemyFood:
    for y in x:
      if True == y:
        enemyFoodList.append((xCounter,yCounter))
      yCounter += 1
    xCounter += 1
    yCounter = 0
  return enemyFoodList

def getClosestFoodPosition(agent,gameState,agentIndex):
  # Gets the position of the food closest to this agent.
  bestDistance = 999999999999
  foodPos = (0,0)
  enemyFoodList = getEnemyFoodList(agent,gameState)
  for pos in enemyFoodList:
    distance = agent.getMazeDistance(pos,gameState.getAgentPosition(agentIndex))
    if distance < bestDistance:
      bestDistance = distance
      foodPos = pos
  return foodPos

def getClosestAgent(agent,position,gameState,agentList):
  bestDistance = 99999999999
  bestAgent = "None"
  for theAgent in agentList:
    print theAgent
    print position
    print gameState.getAgentPosition(theAgent)
    distance = agent.getMazeDistance(position,gameState.getAgentPosition(theAgent))
    if distance < bestDistance:
      bestDistance = distance
      bestAgent = theAgent
  return bestAgent

  # TODO:
  # Finding power pellet,  
