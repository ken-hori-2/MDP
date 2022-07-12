import random
import sys
from env_bp import Environment
import matplotlib.pyplot as plt
import numpy as np
sys.path.append("../")
# from graph_model import Illustration
# from anim_mdp_model import Anim
from statistics import mean, median,variance,stdev
from algorithm_bp import model


# mdp_next_planning_branch.py のアニメーションver, State《 [{}] 》 -> State[{}] (シンプル化)

# mdp_branch_anim.py の整理ver.

# mdp_re.py の整理ver.

# mdp_re_2.py のmodelをclass化したver.

# mdp_model.py の納得度Nの分散を計算させるver.

# mdp_model_N.py のclassの2回呼び出しの修正ver.


class Agent():                              # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    def policy_stressfree(self, state):
        return (self.actions[0])            # UP
    
    def policy_stressfull(self, state):
        return (self.actions[1])            # DOWN
    
    def neuron(self, total_stress, THRESHOLD):# w1 = 1, b = x1*w1

        if THRESHOLD > total_stress: # b:
            print("\n#################################\nStressFree ! UP from here !\n#################################")
            return False
        else:
            print("\n#################################\nStressFull ! DOWN from here !\n#################################")
            return True

    def next_planning(self, N, TRIGAR_COUNT, agent, data):
        N = agent.culculate(data, TRIGAR_COUNT)

        # if N * TRIGAR_COUNT >= 1.0: # 納得度が1.0になるまでリトライ
        if N  >= 1.0:
            print("\n#################################\nDown S0 ! NOT RECONFILM !\n#################################")
            return True
        else:
            print("\n#################################\nDown S0 ! RECONFILM from here !\n#################################")
            return False

    def culculate(self, data, TRIGAR_COUNT):
        mu = mean(data)
        if TRIGAR_COUNT <= 1:
            std = 0.0
        else:
            std = stdev(data)
        print("\ndata:{}".format(data))
        print(" mu:{}".format(mu))
        print(" std:{:.2f}".format(std))

        N = (1.0 - std) * TRIGAR_COUNT
        print(" 納得度N:{}".format(N))
        return N
        


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

    if mod:
        print("\n再確認 (リトライ) 終了しました.\n")



if __name__ == "__main__":
    main()