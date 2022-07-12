import random
import sys
sys.path.append("../")
from env_anim import Environment

import matplotlib.pyplot as plt
import numpy as np
from graph import Illustration
# from anim_class_plt_ver import Anim


# mdp_next_planning_branch.py のアニメーションver, State《 [{}] 》 -> State[{}] (シンプル化)

# mdp_branch_anim.py の整理 ver.

# mdp_re.py の整理ver.


class Agent():                              # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    # def policy(self, state):
    #     return random.choice(self.actions)

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
        # return True * (THRESHOLD <= total_stress)

    def next_planning(self, N, TRIGAR_COUNT):
        if N * TRIGAR_COUNT >= 1.0: # 納得度が1.0になるまでリトライ
            return True
        else:
            print("\n#################################\nDown S0 ! RECONFILM from here !\n#################################")
            return False

    # def culculate(self, action, env, TRIGAR, TOTAL_STRESS, state):
    #     print(action)
    #     next_state, reward, DONE = env.step(action, TRIGAR)
    #     return
        


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

    # Try 10 game.
    for i in range(epoch):
        # Initialize position of agent.
        state = env.reset()
        
        # パラメータ
        TOTAL_STRESS = 0.0
        COUNT = 1 # 0
        TRIGAR_COUNT = 0
        STRESSFREE = 0.0001
        STRESSFULL = 0.3
        TRIGAR = False
        FIRST = True
        DONE = False
        RESULT = False

        # やり直す回数? 納得度の分散度合い
        # 決断の納得しやすさ
        N = 1#0.25 # 1

        # 過程の保存の為の配列
        IGNITION_LIST = np.zeros(shape=10) # env.row_length)
        TOTALREWARD_LIST = np.zeros(shape=50)
        STATE_HISTORY = []
        anim_list = []

        STATE_HISTORY.append(state)
        TOTALREWARD_LIST[0] = TOTAL_STRESS
        while not DONE:
            THRESHOLD = STRESSFULL

            if TOTAL_STRESS <= STRESSFREE or TOTAL_STRESS >= THRESHOLD: # 0に戻った後 または 発火時にTrue
            
                if TOTAL_STRESS <= STRESSFREE and not FIRST:            # 0に戻った後　かつ　初め以外 -> 発火して戻ってきた時
                    
                    TRIGAR_COUNT += 1

                    # 納得度の決定
                    # Nがある程度まで収束したら(小さくなったら)終了 -> branchとか
                    RE = agent.next_planning(N, TRIGAR_COUNT)
                    if RE:
                        break # or branch
                
                # THRESHOLD = agent.next_planning(STRESSFULL, TRIGAR_COUNT)

                TRIGAR = agent.neuron(TOTAL_STRESS, THRESHOLD)
                print(f"TRIGAR : {TRIGAR}")

                FIRST = False
                IGNITION_LIST[TRIGAR_COUNT] = THRESHOLD
            # print(f"THRESHOLD:{IGNITION_LIST}")
            
            if TRIGAR:
                action = agent.policy_stressfull(state)
            else:
                action = agent.policy_stressfree(state)

            print(action)
            print("STEP {} : Agent gets total {:.2f} stress.\n".format(COUNT, TOTAL_STRESS))
            next_state, stress, DONE = env.step(action, TRIGAR)
            TOTAL_STRESS += stress
            state = next_state

            STATE_HISTORY.append(state)
            TOTALREWARD_LIST[COUNT] = TOTAL_STRESS
            COUNT += 1
            if COUNT > 100:
                break

        print("\nEpisode {} : Agent gets {:.2f} stress.\n".format(i, TOTAL_STRESS))
        print("state_history : {}".format(STATE_HISTORY))

    
    # 結果をグラフ化
    RESULT = Illustration(IGNITION_LIST, TOTALREWARD_LIST)
    
    if RESULT:
        print("結果を描写")

    # アニメーション
    # ANIM_RESULT = Anim(STATE_HISTORY)
    # if ANIM_RESULT:
    #     print("アニメーション終了")



if __name__ == "__main__":
    main()