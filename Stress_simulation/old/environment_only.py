from enum import Enum
import numpy as np

import random

from sympy import re


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        return "<State: [{}, {}]>".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column


class Action(Enum):
    UP = 1
    DOWN = -1
    # LEFT = 2
    # RIGHT = -2


class Environment():

    def __init__(self, grid, move_prob=1.0): # 0.8):
        # grid is 2d-array. Its values are treated as an attribute.
        # Kinds of attribute is following.
        #  0: ordinary cell
        #  -1: damage cell (game end)
        #  1: reward cell (game end)
        #  9: block cell (can't locate agent)
        self.grid = grid
        self.agent_state = State()

        # Default reward is minus. Just like a poison swamp.
        # It means the agent has to reach the goal fast!
        self.default_reward = 0 #-0.1 # -0.04

        # Agent can move to a selected direction in move_prob.
        # It means the agent will move different direction
        # in (1 - move_prob).
        self.move_prob = move_prob
        self.reset()

    @property
    def row_length(self):
        return len(self.grid)

    @property
    def column_length(self):
        return len(self.grid[0])

    @property
    def actions(self):
        return [Action.UP, Action.DOWN] #,
                # Action.LEFT, Action.RIGHT]

    @property
    def states(self):
        states = []
        for row in range(self.row_length):
            for column in range(self.column_length):
                # Block cells are not included to the state.
                if self.grid[row][column] != 9:
                    states.append(State(row, column))
        return states

    def transit_func(self, state, action):
        transition_probs = {}
        if not self.can_action_at(state):
            # Already on the terminal cell.
            return transition_probs

        opposite_direction = Action(action.value * -1)

        for a in self.actions:                          # 行動の種類の数だけ回す 1回目:UP, 2回目:DOWN
            # prob = 1.0 # 確実に遷移
            prob = 0
            if a == action:
                prob = self.move_prob
            elif a != opposite_direction:
                prob = (1 - self.move_prob) / 2

            next_state = self._move(state, a)
            # print(a, self.actions)
            print("next state 0 :{}".format(next_state))
            # print(f"trans_probs 0 :{transition_probs}")
            if next_state not in transition_probs:      # next_stateを初めて入れる時(UPの確率を代入)
                transition_probs[next_state] = prob
            else:                                       # next_stateを追加する時(DOWNの確率を代入)
                transition_probs[next_state] += prob

            
            # print(f"trans_probs 1 :{transition_probs}")
            # print("next state 1 :{}\n".format(next_state))

        return transition_probs

    def can_action_at(self, state):                     # 行動できる場所(状態)かどうかを判定する関数を定義
        if self.grid[state.row][state.column] == 0:
            return True
        else:
            return False

    def _move(self, state, action):                     # ある状態である行動をすると、次にどの状態になるかを返す関数を定義
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")

        next_state = state.clone()

        # Execute an action (move).
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        # elif action == Action.LEFT:
        #     next_state.column -= 1
        # elif action == Action.RIGHT:
        #     next_state.column += 1

        # Check whether a state is out of the grid.
        if not (0 <= next_state.row < self.row_length):
            next_state = state
        if not (0 <= next_state.column < self.column_length):
            next_state = state

        # Check whether the agent bumped a block cell.
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state

        return next_state

    def reward_func(self, state):                       # 報酬関数を定義
        reward = self.default_reward
        done = False

        # Check an attribute of next state.
        attribute = self.grid[state.row][state.column]
        if attribute == 1:
            # Get reward! and the game ends.
            reward = 1
            done = True
        elif attribute == -1:
            # Get damage! and the game ends.
            reward = -1
            done = True

        return reward, done

    def reset(self):                                    # エージェントの位置を初期化する関数を定義
        # Locate the agent at lower left corner.
        # self.agent_state = State(self.row_length - 1, 0)
        self.agent_state = State(self.row_length - 2, 0)
        return self.agent_state

    
    
    
    
    
    # 主に使っている部分
    
    def step(self, action):                             # 行動を行う関数を定義
        next_state, reward, done = self.transit(self.agent_state, action)
        if next_state is not None:
            self.agent_state = next_state

        return next_state, reward, done

    def transit(self, state, action):                   # 遷移関数を定義
        transition_probs = self.transit_func(state, action)
        # ↑ 遷移確率 prob = 1.0 , 逆方向:0.0
        print("trans:{}".format(transition_probs))

        if len(transition_probs) == 0:
            return None, None, True

        next_states = []
        probs = []
        for s in transition_probs:
            next_states.append(s)
            probs.append(transition_probs[s])

        # print("next states:{}\n".format(next_states))
        next_state = np.random.choice(next_states, p=probs)
        print("next state:{}".format(next_state))
        reward, done = self.reward_func(next_state)
        print("reward {} {}\n".format(reward, done))
        return next_state, reward, done