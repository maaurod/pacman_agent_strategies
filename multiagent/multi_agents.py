# multi_agents.py
# --------------
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


from util import manhattan_distance
from game import Directions, Actions
from pacman import GhostRules
import random, util
from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        Just like in the previous project, get_action takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legal_moves = game_state.get_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = random.choice(best_indices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (new_food) and Pacman position after moving (new_pos).
        new_scared_times holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        food_right_now = current_game_state.get_food().as_list()
        new_game_state = current_game_state.generate_pacman_successor(action)
        new_pos = new_game_state.get_pacman_position()
        # Distance to closest (CURRENT) food
        distances = [manhattan_distance(new_pos, x) for x in food_right_now]
        min_distance = min(distances) + 0.00001 if distances else 0.00001 # Avoid division by zero

        new_food = new_game_state.get_food()
        # Distance to closest (NEW) food
        new_food_coordinates = new_food.as_list() 
        new_distances = [manhattan_distance(new_pos, x) for x in new_food_coordinates]
        new_min_distance = min(new_distances) - 0.01 if new_distances else -0.01 

        new_ghost_states = new_game_state.get_ghost_states()
        new_ghost_positions = [ghost.get_position() for ghost in new_ghost_states]
        new_ghost_distances = [manhattan_distance(new_pos, x) for x in new_ghost_positions]
        new_min_ghost_distance = min(new_ghost_distances) + 0.01 if new_ghost_distances else 0.01

        # capsules = current_game_state.get_capsules()
        # distances_to_capsules = [manhattan_distance(new_pos, x) for x in capsules]
        # min_distance_to_capsules = min(distances_to_capsules) + 0.01 if distances_to_capsules else 0.01

        new_scared_times = [ghostState.scared_timer for ghostState in new_ghost_states]        
        aux = 1 if min(new_scared_times) <= 0 else 0.25

        score = (1 / min_distance) + (0.2 / new_min_distance) - (4/new_min_ghost_distance)*(aux)
        # Add random noise to the score (exploration)
        return score + random.random() * 1
        

def score_evaluation_function(current_game_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return current_game_state.get_score()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, eval_fn='score_evaluation_function', depth='2'):
        super().__init__()
        self.index = 0 # Pacman is always agent index 0
        self.evaluation_function = util.lookup(eval_fn, globals())
        self.depth = int(depth) 

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action from the current game_state using self.depth
        and self.evaluation_function.

        Here are some method calls that might be useful when implementing minimax.

        game_state.get_legal_actions(agent_index):
        Returns a list of legal actions for an agent
        agent_index=0 means Pacman, ghosts are >= 1

        game_state.generate_successor(agent_index, action):
        Returns the successor game state after an agent takes an action

        game_state.get_num_agents():
        Returns the total number of agents in the game

        game_state.is_win():
        Returns whether or not the game state is a winning state

        game_state.is_lose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        actual_depth = 0
        _, action = self.max_value(game_state, actual_depth)
        return action
    
    def game_terminal(self, game_state, actual_depth):
        return self.depth == actual_depth or game_state.is_win() or game_state.is_lose()
    
    def max_value(self, game_state, actual_depth):
        if self.game_terminal(game_state, actual_depth):
            return self.evaluation_function(game_state), None
        v = float('-inf')
        move = None
        for action in game_state.get_legal_actions(self.index):
            successor_state = game_state.generate_successor(self.index, action)
            v2, _ = self.min_value(1, successor_state, actual_depth)  # Go to the first ghost
            if v2 > v:
                v, move = v2, action
        return v, move

    def min_value(self, agent_index, game_state, actual_depth):
        if self.game_terminal(game_state, actual_depth):
            return self.evaluation_function(game_state), None
        v = float('+inf')
        move = None
        for action in game_state.get_legal_actions(agent_index):
            successor_state = game_state.generate_successor(agent_index, action)
            if agent_index == game_state.get_num_agents() - 1:  # Last ghost moves, Pacman's turn next
                depth_passed = actual_depth + 1
                v2, _ = self.max_value(successor_state, depth_passed)  # Increment depth after all agents moved
            else:
                v2, _ = self.min_value(agent_index + 1, successor_state, actual_depth)  # Go to the next ghost
            if v2 < v:
                v, move = v2, action
        return v, move
    

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action using self.depth and self.evaluation_function
        """
        "*** YOUR CODE HERE ***"
        actual_depth = 0
        _, action = self.max_value(game_state, actual_depth, float('-inf'), float('+inf'))
        return action

    def game_terminal(self, game_state, actual_depth):
        return self.depth == actual_depth or game_state.is_win() or game_state.is_lose()
    
    def max_value(self, game_state, actual_depth, alpha, beta):
        if self.game_terminal(game_state, actual_depth):
            return self.evaluation_function(game_state), None
        v = float('-inf')
        move = None
        for action in game_state.get_legal_actions(self.index):
            successor_state = game_state.generate_successor(self.index, action)
            v2, _ = self.min_value(1, successor_state, actual_depth, alpha, beta)  # Go to the first ghost
            if v2 > v:
                v, move = v2, action
            if v > beta:
                return v, move
            alpha = max(alpha, v)
        return v, move

    def min_value(self, agent_index, game_state, actual_depth, alpha, beta):
        if self.game_terminal(game_state, actual_depth):
            return self.evaluation_function(game_state), None
        v = float('+inf')
        move = None
        for action in game_state.get_legal_actions(agent_index):
            successor_state = game_state.generate_successor(agent_index, action)
            if agent_index == game_state.get_num_agents() - 1:  # Last ghost moves, Pacman's turn next
                depth_passed = actual_depth + 1
                v2, _ = self.max_value(successor_state, depth_passed, alpha, beta)  # Increment depth after all agents moved
            else:
                v2, _ = self.min_value(agent_index + 1, successor_state, actual_depth, alpha, beta)  # Go to the next ghost
            if v2 < v:
                v, move = v2, action
            if v < alpha:
                return v, move
            beta = min(beta, v)
        return v, move


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluation_function

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raise_not_defined()

def better_evaluation_function(current_game_state):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raise_not_defined()
    


# Abbreviation
better = better_evaluation_function
