import numpy as np
from graph_bp import Illustration


class model():

    def __init__(self, epoch, env, agent):
        self.epoch = epoch
        self.env = env
        self.agent = agent
        self.execute()

    def execute(self):
        # Try 10 game.
        for i in range(self.epoch):
            # Initialize position of agent.
            state = self.env.reset()
            
            # Initialize parameter
            TOTAL_STRESS = 0.0
            COUNT = 1 # 0
            TRIGAR_COUNT = 0
            STRESSFREE = 0.01 #0001
            STRESSFULL = 0.3
            TRIGAR = False
            FIRST = True
            DONE = False

            # 納得度の分散度合い 決断の納得しやすさ
            N = 0.25 # 1 # N -> belief? or doubt?
            data = []

            # 過程の保存の為の配列
            IGNITION_LIST = np.zeros(shape=10) # env.row_length)
            TOTALREWARD_LIST = np.zeros(shape=50)
            STATE_HISTORY = []
            anim_list = []

            STATE_HISTORY.append(state)
            TOTALREWARD_LIST[0] = TOTAL_STRESS
            RE = False
            
            
            while not DONE:
                THRESHOLD = STRESSFULL

                if TOTAL_STRESS <= STRESSFREE or TOTAL_STRESS >= THRESHOLD: # 0に戻った後 または 発火時にTrue

                    if TOTAL_STRESS >= STRESSFULL:
                        # 一試行のストレス値の総和
                        epoch_sum = TOTAL_STRESS # 0.3
                        print("epoch sum:{:.2f}".format(epoch_sum))
                
                    if TOTAL_STRESS <= STRESSFREE and not FIRST:            # 0に戻った後　かつ　初め以外 -> 発火して戻ってきた時
                        
                        TRIGAR_COUNT += 1

                        # 納得度の決定 一回の試行のストレス値の総和を追加
                        data.append(epoch_sum) # 0.3
                        RE = self.agent.next_planning(N, TRIGAR_COUNT, self.agent, data) # Nがある程度まで収束したら(小さくなったら)終了 -> branchとか
                        if RE:
                            break # or branch
                    
                    # THRESHOLD = agent.next_planning(STRESSFULL, TRIGAR_COUNT)

                    TRIGAR = self.agent.neuron(TOTAL_STRESS, THRESHOLD)
                    # print(f"TRIGAR : {TRIGAR}")
                    FIRST = False
                    IGNITION_LIST[TRIGAR_COUNT] = THRESHOLD
                # print(f"THRESHOLD:{IGNITION_LIST}")
                
                # UP or DOWN
                if TRIGAR:
                    action = self.agent.policy_stressfull(state)
                else:
                    action = self.agent.policy_stressfree(state)

                print(action)
                print("STEP {} : Agent gets total {:.2f} stress.\n".format(COUNT, TOTAL_STRESS))
                next_state, stress, DONE = self.env.step(action, TRIGAR)
                TOTAL_STRESS += stress
                state = next_state

                STATE_HISTORY.append(state)
                TOTALREWARD_LIST[COUNT] = TOTAL_STRESS
                COUNT += 1
                if COUNT > 100:
                    break

            # print("\nEpisode {} : Agent gets {:.2f} stress.\n".format(COUNT, TOTAL_STRESS))
            print("state_history : {}".format(STATE_HISTORY))


            # 結果をグラフ化

            Illustration(IGNITION_LIST, TOTALREWARD_LIST)

        return True