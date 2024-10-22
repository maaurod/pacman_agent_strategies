# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# # Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in search_agents.py).
"""
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in obj-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem.
        """
        util.raise_not_defined()

    def is_goal_state(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_not_defined()

    def get_successors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_not_defined()

    def get_cost_of_actions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_not_defined()


def tiny_maze_search(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# def addSuccessors(problem, addCost=True):

class SearchNode:
    def __init__(self, parent, node_info):
        """
            parent: parent SearchNode.

            node_info: tuple with three elements => (coord, action, cost)

            coord: (x,y) coordinates of the node position

            action: Direction of movement required to reach node from
            parent node. Possible values are defined by class Directions from
            game.py

            cost: cost of reaching this node from the starting node.
        """

        self.__state = node_info[0]
        self.action = node_info[1]
        self.cost = node_info[2] if parent is None else node_info[2] + parent.cost
        self.parent = parent

    # The coordinates of a node cannot be modified, se we just define a getter.
    # This allows the class to be hashable.
    @property
    def state(self):
        return self.__state

    def get_path(self):
        path = []
        current_node = self
        while current_node.parent is not None:
            path.append(current_node.action)
            current_node = current_node.parent
        path.reverse()
        return path
    
    # Consider 2 nodes to be equal if their coordinates are equal (regardless of everything else)
    # def __eq__(self, __o: obj) -> bool:
    #     if (type(__o) is SearchNode):
    #         return self.__state == __o.__state
    #     return False

    # # def __hash__(self) -> int:
    # #     return hash(self.__state)

def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.get_start_state())
    print("Is the start a goal?", problem.is_goal_state(problem.get_start_state()))
    print("Start's successors:", problem.get_successors(problem.get_start_state()))
    """

    # Define useful variables and objects
    stack = util.Stack()
    visited = set()

    state = problem.get_start_state()
    stack.push(SearchNode(None, (state, None, 0)))
    
    # Loop until the stack is empty or the goal is reached
    while not stack.is_empty():
        # Pop node from stack's top
        current_node = stack.pop()

        # Check if goal state
        if problem.is_goal_state(current_node.state):
            return current_node.get_path() # Path reconstruction

        # Else, add to visited
        visited.add(current_node.state)

        # Add successors to stack
        successors = problem.get_successors(current_node.state)
        for successor in successors:
            # Check if node has been visited
            if successor[0] not in visited:
                stack.push(SearchNode(current_node, successor)) # Push SearchNode class object to stack


def breadth_first_search(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Define useful variables and objects
    queue = util.Queue()
    visited = set()

    state = problem.get_start_state()
    queue.push(SearchNode(None, (state, None, 0)))
    
    # Loop until the queue is empty or the goal is reached
    while not queue.is_empty():
        # Pop node from the queue's top
        current_node = queue.pop()

        # Check if goal state
        if problem.is_goal_state(current_node.state):
            return current_node.get_path() # Path reconstruction

        # Else, add to visited
        visited.add(current_node.state)

        # Add successors to stack
        successors = problem.get_successors(current_node.state)
        for successor in successors:
            # Check if node has been visited
            if successor[0] not in visited:
                queue.push(SearchNode(current_node, successor)) # Push SearchNode class object to the queue

def uniform_cost_search(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Define useful variables and objects
    queue = util.PriorityQueue()
    visited = set()

    state = problem.get_start_state()
    queue.push(SearchNode(None, (state, None, 0)), 0)
    
    # Loop until the queue is empty or the goal is reached
    while not queue.is_empty():
        # Pop node from queue's top
        current_node = queue.pop()

        # Check if goal state
        if problem.is_goal_state(current_node.state):
            return current_node.get_path() # Path reconstruction

        # Else, add to visited
        visited.add(current_node.state)

        # Add successors to queue
        successors = problem.get_successors(current_node.state)
        for successor in successors:
            # Check if node has been visited
            if successor[0] not in visited:
                queue.update(SearchNode(current_node, successor), current_node.cost + successor[2]) # Update SearchNode class object to queue

def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def a_star_search(problem, heuristic=null_heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # We define priority queue data structure
    priority_queue = util.PriorityQueue()
    # Dictionary to keep track of visited nodes (and minimum costs as these are not accessible from the priority queue structure)
    found_costs = dict()

    # Initialize search
    initial_state = problem.get_start_state()
    found_costs[initial_state] = 0
    priority_queue.push(SearchNode(None, (initial_state, None, 0)), 0)

    while not priority_queue.is_empty():
        # Expand node
        expanded_node = priority_queue.pop()
        expanded_state = expanded_node.state

        if problem.is_goal_state(expanded_state):
            return expanded_node.get_path()
                
        # Add nodes to frontier (priority queue)
        successors = problem.get_successors(expanded_state)
        for successor_info in successors:
            new_state, new_action, new_cost = successor_info
            
            # Current cost to reach the successor node
            cost_to_new_state = found_costs[expanded_state] + new_cost
            
            if new_state not in found_costs or cost_to_new_state < found_costs[new_state]:
                # Heuristic cost to reach the goal from the successor node
                h_n = heuristic(new_state, problem)
                f_n = cost_to_new_state + h_n

                found_costs[new_state] = cost_to_new_state
                new_node = SearchNode(expanded_node, (new_state, new_action, cost_to_new_state)) 
                priority_queue.update(new_node, f_n)

    return None
    

# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search