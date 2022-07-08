import random

from numpy import full
from env_next_planning import Environment

import matplotlib.pyplot as plt
import numpy as np
from graph import Illustration


class Agent():                              # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)

    def policy_stressfree(self, state):
        return (self.actions[0])            # UP
    
    def policy_stressfull(self, state):
        return (self.actions[1])            # DOWN
    
    def neuron(self, total_stress, threshold):# w1 = 1, b = x1*w1

        if threshold > total_stress: # b:
            print("thre:{}  total_stress:{}".format(threshold, total_stress))
            print("#################################\nStressFree ! UP from here !\n#################################")
            return False
        else:
            print("#################################\nStressFull ! DOWN from here !\n#################################")
            return True
        # return True * (threshold <= total_stress)

    def next_planning(self, STRESSFULL, trigar_count):
        return (STRESSFULL + (0.1*trigar_count))

    def all_green(self, total_reward, STRESSFREE, threshold):
        if total_reward < STRESSFREE or total_reward >= threshold:
            # print("########################################################  {} total:{}".format(FIRST, total_reward))
            # if total_reward < STRESSFREE and FIRST==False:
            #         trigar_count += 1
                    # print("########################################################")
            # FIRST = False

            return True# , trigar_count, FIRST
        else:
            return False#, trigar_count, FIRST
        


def main():                                 # 環境内でエージェントを動作させるコードを実装
    N = int(input("試行回数 N = "))
    # Make grid environment.
    grid = [
        [1],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0], # start
        [-1]
    ]
    
    env = Environment(grid)
    agent = Agent(env)

    # Try 10 game.
    for i in range(N):
        # Initialize position of agent.
        state = env.reset()
        total_reward = 0
        done = False
        count = 0
        TRIGAR = False
        trigar_count = 0
        FIRST = True
        STRESSFREE = 0.01#0.0001
        STRESSFULL = 0.3
        IGNITION_LIST = np.zeros(shape=10) # env.row_length)
        TOTALREWARD_LIST = np.zeros(shape=101)
        RESULT = False
        # print("RESULT:{}".format(RESULT))
        # continue_move_complete = False

        while not done:
            continue_move_complete = False

            threshold = STRESSFULL
            # continue_move_complete, trigar_count, FIRST = agent.all_green(round(total_reward, 2), STRESSFREE, threshold, trigar_count, FIRST)
            continue_move_complete = agent.all_green(round(total_reward, 2), STRESSFREE, threshold)

            if continue_move_complete:
                
                if total_reward < STRESSFREE and FIRST==False:
                    trigar_count += 1
                threshold = (STRESSFULL + (0.1*trigar_count)) # agent.next_planning(STRESSFULL, trigar_count)

                TRIGAR = agent.neuron(total_reward, threshold)
                print(f"####TRIGAR:{TRIGAR}####")
                print("trigar_count:{}".format(trigar_count))
                IGNITION_LIST[trigar_count] = threshold
                FIRST = False
            print(f"threshold:{IGNITION_LIST}")
            
            if TRIGAR:
               
                action = agent.policy_stressfull(state)
                print(action)
                next_state, reward, done = env.step(action, TRIGAR)
                total_reward += reward
                state = next_state
                
                print("Step {}: Agent gets total {:.2f} stress.\n".format(count, total_reward))
            else:
                action = agent.policy_stressfree(state)
                print(action)
                next_state, reward, done = env.step(action, TRIGAR)
                total_reward += reward
                state = next_state

                print("Step {}: Agent gets total {:.2f} stress.\n".format(count, total_reward))

            TOTALREWARD_LIST[count] = total_reward
            count += 1
            if count > 100:
                break

        print("\nEpisode {}: Agent gets {:.2f} stress.\n".format(i, total_reward))

    
    # 結果をグラフ化
    RESULT = Illustration(IGNITION_LIST, TOTALREWARD_LIST)
    
    if RESULT:
        print("結果を描写")
        # plt.show()


if __name__ == "__main__":
    main()