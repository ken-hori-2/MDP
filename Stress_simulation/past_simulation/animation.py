import math
import random
import copy
import matplotlib.pyplot as plt
from matplotlib import animation, rc, gridspec
from IPython.display import HTML
import numpy as np
from soupsieve import match

N = 1  # エージェントの個数
SIZE = N   # 仮想空間のサイズ
TIMELIMIT = 5 # 40 #10  # シミュレーションの打ち切り時刻
SEED = 65535  # 乱数の初期化
# R = 15  # 感染範囲
SPEED = N/20  # エージェントの歩幅
TREATMENT_PERIOD = 0 # 10  # 感染してから治るまでの期間
OVER_CAPACITY = N/2  # 感染拡大の目安
TRIGAR = 0 # 2
NODE = np.zeros(shape=10)
# NODE = [1, 1, 0, 1, 0, 0] # [1, 1, 0, 0, 0]
NODE = [1, 1, 0, 0, 1] # [1, 1, 0, 0, 0]
# NODE = [1, 1, 0, 0, 1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1]
STRESS = [0] # np.zeros(shape=10)
STEPS = [0]
MATCH = [0]
OVER_CAPACITY2 = 1  # 感染拡大の目安

OVER_CAPACITY3 = [0]

#Agent class
class Agent:
    
    def __init__(self, state):
        self.state = state  # 状態の設定（S or I or R or D）
        self.y = 0 #random.randint(1,SIZE)  # x座標の初期値
        self.x = 0.0 #random.randint(1,SIZE)  # y座標の初期値
        radian = math.radians(random.randint(1,360))
        self.y_v = 0#SPEED #0.01#math.cos(radian)*SPEED  # x方向の速さ
        # self.y_v = 0#math.sin(radian)*SPEED  # y方向の速さ
        self.term = 0  # 感染してからの日数

        self.stress = 0 # ストレス値
        self.steps = 0

        self.match = 0
        self.match_rate = 0
        
        # self.mortality = random.random()  # 感染した場合生き残れるかどうかのID

    def _calcnext(self, agents):  # 次時刻の計算
        if self.state == "S":
            self._state_S(agents)  # 状態S用の計算
        elif self.state == "I":
            self._state_I()  # 状態I用の計算
        elif self.state == "R":
            self._state_R()  # 状態R用の計算

    def _update_xy(self):
        """
        エージェントのxy座標を更新する
        """
        # if self.y + self.y_v < 0:
        #     self.y = 0
        #     # self.x_v *= -1
        #     self.state = "S"
            
        # if SIZE < self.y + self.y_v:
        #     # self.x_v *= 0 #-1
        #     self.y = 0 #self.x_v

        # if stress_decision == True:
        
        # コメントアウト
        if self.state == "I" or self.state == "S":
            self.y = self.y + self.y_v #* self.control_f

        if self.state == "R":
            # self.x_v *= -1
            self.y = (self.y - self.y_v) #*= -1


    def _state_S(self, agents):  # 状態Sの計算メソッド
        
        if self.stress > TREATMENT_PERIOD:  # 一定の感染日数が経つと免疫を獲得する
            self.state = "I"
        elif NODE[self.steps] == 0:
            self.stress += 1
        elif NODE[self.steps] == 1:
            self.match += 1
        
        # xy座標を更新
        print("一致数:{} ステップ数:{}".format(self.match, self.steps))

        self.steps += 1

        STRESS[0] = self.stress
        STEPS[0] = self.steps

        MATCH[0] = self.match
        self._update_xy()

    def _state_I(self):  # 状態Iの計算メソッド

        self.match_rate = self.match / (self.steps-1)
        print('rate:{}%'.format(self.match_rate*100))
        if self.match_rate >= 0.5:
            self.term = 1  # 発見率によって閾値変更 今は手動
        elif self.match_rate >= 0.8:
            self.term = 2
        OVER_CAPACITY3[0] = self.term

        if NODE[self.steps] == 1: # 0620 追加
            # TRIGAR = self.term + 1
            self.term += 1
            self.match += 1
        # if self.term > TRIGAR: # 0 : # TREATMENT_PERIOD:  # 一定の感染日数が経つと免疫を獲得する
        #     self.state = "R"
        if self.stress > self.term: #TREATMENT_PERIOD:  # 一定の感染日数が経つと免疫を獲得する
            self.state = "R"
        elif NODE[self.steps] == 0: # 0620 追加
            # self.term += 1  # 感染日数を追加
            self.stress += 1

        self.steps += 1

        STRESS[0] = self.stress
        STEPS[0] = self.steps
        MATCH[0] = self.match

        # xy座標を更新
        self._update_xy()

    def _state_R(self):  # 状態Rの計算メソッド
        # xy座標を更新
        self._update_xy()

  # agentクラスの定義終わり


def calcn(agents):
    """次時刻の状態を計算"""
    # 状態Sのデータ
    xlistS, ylistS = [], []
    # 状態Iのデータ
    xlistI, ylistI = [], []
    # 状態Rのデータ
    xlistR, ylistR = [], []

    for i in range(len(agents)):
        agents[i]._calcnext(agents)
        # a[i].putstate()
        # グラフデータに現在位置を追加
        if agents[i].state == "S":
            xlistS.append(agents[i].x)
            ylistS.append(agents[i].y)
        elif agents[i].state == "I":
            xlistI.append(agents[i].x)
            ylistI.append(agents[i].y)
        elif agents[i].state == "R":
            xlistR.append(agents[i].x)
            ylistR.append(agents[i].y)

    return xlistS, ylistS, xlistI, ylistI, xlistR, ylistR
    # calcn()関数の終わり


def scatter_plot(image, n, xlistS, ylistS, xlistI, ylistI, xlistR, ylistR):
    """散布図描画用関数"""
    image += ax[n].plot(xlistS, ylistS, "^", markersize=20, label="Forword", color="b", alpha=0.5) #状態Sのプロット
    image += ax[n].plot(xlistI, ylistI, "o", markersize=20, label="Stay", color="y") #状態Iのプロット
    image += ax[n].plot(xlistR, ylistR, "v", markersize=20, label="Backword", color="r", alpha=0.5) #状態Rのプロット
    return image

# 初期化
random.seed(SEED) # 乱数の初期化
# 状態SのエージェントをN個生成
agentsA = [Agent("S") for i in range(N)]

# 状態Iのエージェントの設定
agentsA[0].state = "S" # "I"
agentsA[0].x = SIZE/2
agentsA[0].y = SIZE/2
agentsA[0].control_f = 1

# グラフデータの初期化
T = []
# Statas数推移
statasS_sum_left= []
statasI_sum_left= []
statasR_sum_left= []
# statasS_sum_right= []
# statasI_sum_right= []
# statasR_sum_right= []

#描画するグラフの設定
fig = plt.figure(figsize=(7.5,5))
gs = gridspec.GridSpec(2, 2, height_ratios=(3, 1))
ax = [plt.subplot(gs[0, 0]), plt.subplot(gs[1, 0]), plt.subplot(gs[0, 1]), plt.subplot(gs[1, 1])]
#空のグラフが出てしまうのを回避
# plt.close()

#アニメーション用のグラフ保管場所
ims = []

legend_flag = True  # 凡例描画のフラグ
control_flag = True  # 自粛宣言したか

x = [1,2,3]
# x = np.arange(-1, 1, 0.1) 
y1 = MATCH[0]
y2 = 1-y1 #STEPS # - y1

# エージェントシミュレーション
for t in range(TIMELIMIT):
    T.append(t)
    xlistS, ylistS, xlistI, ylistI, xlistR, ylistR = calcn(agentsA)  # 次時刻の状態を計算
    im = []

    # 左側グラフ（対策なしの表示
    # subplot0：散布図
    im += scatter_plot(im, 0, xlistS, ylistS, xlistI, ylistI, xlistR, ylistR)

    # subplot2：推移図
    statasS_sum_left.append(len(xlistS))
    statasI_sum_left.append(len(xlistI))
    statasR_sum_left.append(len(xlistR))
    im += ax[1].stackplot(T, statasI_sum_left, statasR_sum_left, statasS_sum_left, colors=["y","r", "b"], alpha=0.7)

    # im += ax[2].bar(T, STRESS, colors=["r"], alpha=0.7)
    # STRESS[0] = STRESS[0] + STRESS[0] # ((9/10) ** STRESS[0])
    # im += ax[2].bar(x,STRESS, color=['#66bd63'], width = 0.1)
    
    im += ax[2].bar(x[1], STRESS, color=['orange'], width = 0.5, label="Stress", tick_label="Add Stress")
    im += ax[2].bar(x[0], 0)
    im += ax[2].bar(x[2], 0)
    # im += 
    ax[2].axhline(2, ls = "--", color = "green")
    # im += ax[2].bar(x,STRESS, bottom=STRESS[0], color=['orange'], width = 0.1)

    # ax[3].bar(x[1], 5, color = "blue", width = 0.5, label ="全体", alpha = 0.05)
    im += ax[3].bar(x[1], MATCH, color=['yellow'], width = 0.5, label="一致", alpha = 0.7) # , tick_label="Add Stress") #STRESS, color=['orange'], width = 0.5, label="Stress", tick_label="Add Stress")
    im += ax[3].bar(x[1], 5-MATCH[0], bottom = MATCH, color=['blue'], width = 0.5, label="不一致", alpha = 0.7) # , tick_label="Add Stress")
    # im += ax[3].pie(x2, labels=Label) # , color = CL)
    # im += ax[3].axis('equal')
    im += ax[3].bar(x[0], 0)
    im += ax[3].bar(x[2], 0)
    print("STRESS:{}".format(STRESS[0]))

    #描画設定
    if legend_flag:  # 一回のみ凡例を描画
        ax[0].legend(loc='lower center', bbox_to_anchor=(1.1, 1.1), ncol=4)
        ax[0].set_xlim(0, SIZE)
        ax[0].set_ylim(0, SIZE)
        ax[0].tick_params(labelbottom=False,labelleft=False,labelright=False,labeltop=False, length=0)
        ax[0].tick_params(length=0)
        ax[0].set_title("Agent state process")
        ax[1].tick_params(labelbottom=False,labelleft=True,labelright=False,labeltop=False)
        ax[1].axhline(OVER_CAPACITY, ls = "--", color = "black")

        ax[2].tick_params(labelbottom=False,labelleft=True,labelright=False,labeltop=False)
        ax[2].axhline(OVER_CAPACITY2, ls = "--", color = "black")

        ax[2].set_title("Add stress process")
        ax[2].legend(prop={"size": 10}, loc="best")

        ax[3].set_title("発見率")
        # ax[3].legend(prop={"size": 10}, loc="best")
        legend_flag = False
    time_str = ("t = {}".format(t))
    # im.append(ax[0].text(0.4 + t/50, 0.55, time_str))
    im.append(ax[0].text(0.2, 0.55, time_str))
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval=1000)

plt.show()