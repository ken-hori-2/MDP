from enum import Enum
import numpy as np

import random

from sympy import re


class State():

    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        # return "<State: [{}, {}]>".format(self.row, self.column)
        if self.column == 2:
            return "[{}]".format(-1)
        else:
            return "[{}]".format(self.row)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.column


class Action(Enum): # 進む方向 前・後 左・右
    UP = 1
    DOWN = -1
    RECONFILM = 2
    BRANCH = -2


class Environment():

    def __init__(self, grid, move_prob=1.0): # 0.8):
        
        self.grid = grid
        self.agent_state = State()

        # Default reward is minus. Just like a poison swamp.
        self.default_reward = 0.1

        # Agent can move to a selected direction in move_prob.
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
        return [Action.UP, Action.DOWN,
                Action.RECONFILM, Action.BRANCH]

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
            
            prob = 0
            if a == action:
                # prob = self.move_prob
                prob = 1.0 # 今は確実に遷移
            elif a != opposite_direction:
                # prob = (1 - self.move_prob) / 2
                prob = 0.0 # 今は行かない方向に行く可能性はない

            next_state = self._move(state, a)
            
            if next_state not in transition_probs:      # next_stateを初めて入れる時(UPの確率を代入)
                transition_probs[next_state] = prob
            else:                                       # next_stateを追加する時(DOWNの確率を代入)
                transition_probs[next_state] += prob

            
        return transition_probs

    def can_action_at(self, state):                     # 行動できる場所(状態)かどうかを判定する関数を定義
        if self.grid[state.row][state.column] == 0:
            return True
        
        # add 0715
        elif self.grid[state.row][state.column] == 7:
            return True


        else:
            return False

    def _move(self, state, action):                     # ある状態である行動をすると、次にどの状態になるかを返す関数を定義
        if not self.can_action_at(state):
            raise Exception("Can't move from here!")


        next_state = state.clone()

        # Execute an action (move).                     # transit_func 行動の数だけ回し、_move　で行動全ての次状態を代入
        if action == Action.UP:
            next_state.row -= 1
        elif action == Action.DOWN:
            next_state.row += 1
        elif action == Action.RECONFILM:
            # next_state.column -= 1
            next_state.row -= 1
        elif action == Action.BRANCH:
            if self.grid[next_state.row][2] == -1: # Action.Branchで同じ処理をしている
                next_state.column += 2                        # ここを変更することで、[-1]を追加
                print("\nBRANCH TRUE")
            else:
                print("NO BRANCH !!!!!")

        # Check whether a state is out of the grid.             # 次に選択した行動が場外だったら今の状態に留まる
        if not (0 <= next_state.row < self.row_length):
            next_state = state
        if not (0 <= next_state.column < self.column_length):
            next_state = state

        # Check whether the agent bumped a block cell.          # 次に選択した行動が壁だったら今の状態に留まる
        if self.grid[next_state.row][next_state.column] == 9:
            next_state = state

        return next_state

    def reward_func(self, state, TRIGAR):                       # 報酬関数を定義
        if TRIGAR:
            reward = -self.default_reward
        else:
            reward = self.default_reward
        done = False

        # Check an attribute of next state.
        attribute = self.grid[state.row][1]
        if attribute == 1 and TRIGAR:
            # Get reward! and the game ends.
            print("Node 一致 (On the way back)")
        
            if self.grid[state.row][2] == -1:
                done = True
                print("\n再確認終了 次状態は分岐")


        # コメントアウト
        # attribute_branch = self.grid[state.row][2]
        # if attribute_branch == -1:
        #     # Get damage! and the game ends.
        #     reward = 0 # +1
        #     done = True
        #     print("\n再確認終了\n分岐!!!!!")

            

        return reward, done

    def reset(self):                                            # エージェントの位置を初期化する関数を定義
        # Locate the agent at lower left corner.
        # self.agent_state = State(self.row_length - 1, 0)
        self.agent_state = State(self.row_length - 2, 0)
        return self.agent_state

    
    
    
    
    
    # メイン部分
    
    def step(self, action, TRIGAR):                             # 行動を行う関数を定義
        next_state, reward, done = self.transit(self.agent_state, action, TRIGAR)
        
        if next_state is not None:
            self.agent_state = next_state

        return next_state, reward, done

    def transit(self, state, action, TRIGAR):                   # 遷移関数を定義
        transition_probs = self.transit_func(state, action)
        # ↑ 遷移確率 prob = 1.0 , 逆方向:0.0
        # print("遷移確率:{}".format(transition_probs))
        print("transition probability:{}".format(transition_probs))

        if len(transition_probs) == 0:
            return None, None, True

        next_states = []
        probs = []
        for s in transition_probs:
            next_states.append(s)
            probs.append(transition_probs[s])

        # print("next states:{}\n".format(next_states))
        next_state = np.random.choice(next_states, p=probs)# next_state の確率からランダムで採択
        print("next state:{}".format(next_state))
        reward, done = self.reward_func(next_state, TRIGAR)
        # print("reward {} {}".format(reward, done))
        return next_state, reward, done