import random

from numpy import full
from env import Environment

import matplotlib.pyplot as plt
import numpy as np
from graph import Illustration


class Agent():                              # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    # def policy(self, state):
    #     print(self.actions[1])
    #     return random.choice(self.actions)

    def policy_stressfree(self, state):
        return (self.actions[0])            # UP
    
    def policy_stressfull(self, state):
        return (self.actions[1])            # DOWN
    
    def neuron(self, total_stress, threshold):# w1 = 1, b = x1*w1

        if threshold > total_stress: # b:
            print("#################################\nStressFree ! UP from here !\n#################################")
            return False
        else:
            print("#################################\nStressFull ! DOWN from here !\n#################################")
            return True
    
    # def step(total_stress):
    #     return 1.0 * (total_stress >= 0.0)


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
        STRESSFREE = 0.0001
        STRESSFULL = 0.3
        IGNITION_LIST = np.zeros(shape=10) # env.row_length)
        TOTALREWARD_LIST = np.zeros(shape=101)
        RESULT = False

        while not done:
            
            threshold =  (STRESSFULL + (0.1*trigar_count))
            # print(f"threshold:{threshold}")

            if total_reward < STRESSFREE or total_reward >= threshold:
            
                if total_reward < STRESSFREE and not FIRST:
                    trigar_count += 1
                    threshold =  (STRESSFULL + (0.1*trigar_count))

                TRIGAR = agent.neuron(total_reward, threshold)

                FIRST = False
                IGNITION_LIST[trigar_count] = threshold
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