import random
import sys
# sys.path.append("../")
from env_anim import Environment

import matplotlib.pyplot as plt
import numpy as np
from graph_model import Illustration
# from anim_class_plt_ver import Anim
from statistics import mean, median,variance,stdev
from algorithm import model


# mdp_next_planning_branch.py のアニメーションver, State《 [{}] 》 -> State[{}] (シンプル化)

# mdp_branch_anim.py の整理ver.

# mdp_re.py の整理ver.

# mdp_re_2.py のmodelをclass化したver.


class Agent():                              # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    def policy_stressfree(self, state):
        return (self.actions[0])            # UP
    
    def policy_stressfull(self, state):
        return (self.actions[1])            # DOWN

    # def policy_retry(self, state):
    #     return (self.actions[2])
    # def policy_branch(self, state):
    #     return (self.actions[3])
    
    def neuron(self, total_stress, THRESHOLD):# w1 = 1, b = x1*w1

        if THRESHOLD > total_stress: # b:
            print("\n#################################\nStressFree ! UP from here !\n#################################")
            return False
        else:
            print("\n#################################\nStressFull ! DOWN from here !\n#################################")
            return True

    def next_planning(self, N, TRIGAR_COUNT):
        if N * TRIGAR_COUNT >= 1.0: # 納得度が1.0になるまでリトライ
            return True
        else:
            print("\n#################################\nDown S0 ! RECONFILM from here !\n#################################")
            return False

    # def culculate(self, data):
    #     mu = mean(data)
    #     std = stdev(data)
    #     print("\ndata:{}".format(data))
    #     print(" mu:{}".format(mu))
    #     print(" std:{:.2f}".format(std))

    #     N = 1.0 - std
    #     print(" 納得度N:{}".format(N))
    #     return N
        


def main():                                 # 環境内でエージェントを動作させるコードを実装
    epoch = int(input("試行回数 N = "))
    # Make grid environment.
    grid = [
        [0],
        [0],
        [0],
        [0], # start
        [-1]
    ]
    
    env = Environment(grid)
    agent = Agent(env)

    
    mod = model(epoch, env, agent)
    IGNITION_LIST, TOTALREWARD_LIST = mod.execute() # IGNITION_LIST, TOTALREWARD_LIST = model(env, agent)
    
    # 結果をグラフ化
    RESULT = False
    
    RESULT = Illustration(IGNITION_LIST, TOTALREWARD_LIST)
    
    if RESULT:
        print("結果を描写")



if __name__ == "__main__":
    main()