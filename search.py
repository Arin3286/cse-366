# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from util import*
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    frontier = util.Stack()
    visited = set()
    frontier.push((problem.getStartState(), [], 0))  # (state, path, cost)

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                frontier.push((successor, path + [action], cost + stepCost))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    visited = set()
    frontier.push((problem.getStartState(), [], 0))

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited:
            visited.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                frontier.push((successor, path + [action], cost + stepCost))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    visited = {}
    frontier.push((problem.getStartState(), [], 0), 0)  # (state, path, cost), priority=cost

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()
        if problem.isGoalState(state):
            return path
        if state not in visited or visited[state] > cost:
            visited[state] = cost
            for successor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost
                frontier.push((successor, path + [action], newCost), newCost)
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    """ Search the shallowest nodes in the search tree first. """
    currPath = []           # The path that is popped from the frontier in each loop
    currState =  problem.getStartState()    # The state(position) that is popped for the frontier in each loop
    print(f"currState: {currState}")
    if problem.isGoalState(currState):     # Checking if the start state is also a goal state
        return currPath

    frontier = Queue()
    frontier.push( (currState, currPath) )     # Insert just the start state, in order to pop it first
    explored = set()
    while not frontier.isEmpty():
        currState, currPath = frontier.pop()    # Popping a state and the corresponding path
        # To pass autograder.py question2:
        if problem.isGoalState(currState):
            return currPath
        explored.add(currState)
        frontierStates = [ t[0] for t in frontier.list ]
        for s in problem.getSuccessors(currState):
            if s[0] not in explored and s[0] not in frontierStates:
                # Lecture code:
                # if problem.isGoalState(s[0]):
                #     return currPath + [s[1]]
                frontier.push( (s[0], currPath + [s[1]]) )      # Adding the successor and its path to the frontier

    return []       # If this point is reached, a solution could not be found.


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue  # Ensure you have a PriorityQueue implemented or imported

    # Initialize the priority queue
    frontier = PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)  # (state, path, cost), priority = cost

    # Keep track of visited states and their costs
    visited = {}

    while not frontier.isEmpty():
        # Pop the node with the lowest cost
        state, path, cost = frontier.pop()

        # If the current state is the goal, return the path
        if problem.isGoalState(state):
            return path

        # If the state has not been visited, process it
        if state not in visited or visited[state] > cost:
            visited[state] = cost  # Mark this state as visited with the current cost

            # Expand the current state
            for successor, action, stepCost in problem.getSuccessors(state):
                newCost = cost + stepCost  # Calculate the cumulative cost
                newPath = path + [action]  # Update the path
                frontier.push((successor, newPath, newCost), newCost)  # Push to queue with priority = cost

    # If no solution is found, return failure
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
