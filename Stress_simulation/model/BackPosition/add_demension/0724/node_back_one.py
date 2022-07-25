from cmath import pi
from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import random

from numpy.core.defchararray import title
from pytest import skip
from tenacity import retry
from torch import ne
from urllib3 import Retry

# add_0523_2_branch.py == add_branch.py

# add_branch_failed_2.py == add_branch_failed_2_v2.py

# 初期位置での迷路の様子

# 図を描く大きさと、図の変数名を宣言

# # 現在地S0に緑丸を描画する
# line, = ax.plot([2.5], [3.5], marker="o", color='g', markersize=30)
fig = plt.figure(figsize=(2, 7))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
plt.text(0.5, 4.5, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 6.5, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 8.5, 'Node\n(事前情報)', size=8, ha='center')

# plt.text(0.5, 1.3, 'Node\n(事前情報)', size=8, ha='center')
plt.text(0.5, 0.3, 'Node\n(事前情報)', size=8, ha='center')

plt.plot([0.5, 0.5], [0.0, 8.5],color="black")
#plt.text(4.5, 0.3, 'GOAL', ha='center')

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 9)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

# line3, = ax.plot([0.5], [1.5], marker="o", color='m', markersize=40)
line3, = ax.plot([0.5], [0.5], marker="o", color='m', markersize=40)
line4, = ax.plot([0.5], [4.5], marker="o", color='m', markersize=40)
line5, = ax.plot([0.5], [6.5], marker="o", color='m', markersize=40)
line6, = ax.plot([0.5], [8.5], marker="o", color='m', markersize=40)

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [0.5], marker="^", color='y', markersize=20)
line1, = ax.plot([0.5], [0.5], marker="*", color='r', markersize=20)
line2, = ax.plot([0.5], [0.5], marker="*", color='b', markersize=20)
line7, = ax.plot([0.5], [0.5], marker="*", color='g', markersize=20)



# 初期の方策を決定するパラメータtheta_0を設定

# 行は状態0～7、列は移動方向で↑、→、↓、←を表す
theta_0 = np.array([[1, np.nan, np.nan, np.nan],  # s0
                    [1, np.nan, np.nan, np.nan],  # s1
                    [1, np.nan, np.nan, np.nan],  # s2
                    [1, np.nan, np.nan, np.nan],  # s3
                    [1, 5, np.nan, np.nan],  # s4
                    [1, np.nan, np.nan, np.nan],  # s5
                    [1, 5, np.nan, np.nan],  # s6
                    [1, np.nan, np.nan, np.nan],  # s7、※ LandMark
                    [1, 5, np.nan, np.nan]  #s8
                    ])

# 方策パラメータthetaを行動方策piに変換する関数の定義


def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''

    [m, n] = theta.shape  # thetaの行列サイズを取得
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])  # 割合の計算

    pi = np.nan_to_num(pi)  # nanを0に変換

    return pi


# 初期の方策pi_0を求める
# pi_0 = simple_convert_into_pi_from_theta(theta_0)
[m, n] = theta_0.shape  # thetaの行列サイズを取得
# pi_0 = np.zeros((m, n))
pi_0 = np.nan_to_num(theta_0)  # nanを0に変換

# 初期の方策pi_0を表示
pi_0

# 1step移動後の状態sを求める関数を定義
state_history = [0]  # 8 # エージェントの移動を記録するリスト  変更0527

import random

List_sub = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
List = [0.8, 0.9, 1.0, 1.1, 1.2]
SUM = 0
TEST = np.zeros(shape=(1500))
diff = np.zeros(shape=(1500))
Diff2 = np.zeros(shape=(1500))
retry_num = 0
Retry_sum = np.zeros(shape=(1500))
branch = [0, 0, 0]#np.zeros(shape=(3))
true_list = [1, 1, 1]
# Br = np.zeros(shape=(50))
Br = np.zeros((1500, 3))

# node1 = random.randint(0,1)
# node2 = random.randint(0,1)
# print('node1:{}\nnode2:{}'.format(node1,node2))

pi_0[4,2] = 1 #random.randint(0,1)
pi_0[6,2] = 1 #0 #random.randint(0,1)
print('node1:{}\nnode2:{}'.format(pi_0[4,2],pi_0[6,2]))
print(pi_0)

def AAA(s,depth,i,j,SUM, retry_num):
    # direction = ["up", "right", "down", "left"]
    if s == 0: # 1
        branch[2] = 0
        # 追加
        branch[0] = 0
        branch[1] = 0
    # depth += 1
    # print('depth:{}'.format(depth))

    
    if s == 8 or i > 100: # 500
        #####
        print('終了!!!!')
        print('state_history={}'.format(state_history))
        excp = Exception()
        excp.value = state_history, SUM, retry_num
        raise excp
        #####


        if branch[0] == 1 and branch[1] == 1:
            print('No.{} 発見 Goal ! j:{}'.format(s,j))
            # branch[j] = 1 # random.randint(0,1)     # branch のランダムの回数が多い？
            branch[2] = 1 # random.randint(0,1)     # branch のランダムの回数が多い？
            print("branch:{} j:{}".format(branch,j))
            Br[i] = branch

        # branch = [1, 1, 1] の時以外 x > 1.2
        test = 1.3
        TEST[i] = test 
        Diff2[i] = abs(1.0 - test)
        diff[j] = abs(1.0 - test)
        SUM += diff[j]
        
        Br[i] = branch

        if branch == true_list:
            print('Goal 発見 !')
            print('終了!!!!')
            print('state_history={}'.format(state_history))

            # branch = [1, 1, 1] の時のみ x <= 1.2
            test = np.random.choice(List, 1, p=[0.20, 0.20, 0.20, 0.20, 0.20])
            TEST[i] = test 
            Diff2[i] = abs(1.0 - test)
            diff[j] = abs(1.0 - test)
            SUM += diff[j]

            retry_num += 1

            excp = Exception()
            excp.value = state_history, SUM, retry_num
            raise excp
        elif i > 500:
            print('エラー')
            excp = Exception()
            excp.value = state_history, SUM, retry_num
            raise excp

        else:
        # elif retry_num < 20:
            retry_num += 1 # コメントアウト
            
            s_next = s - 3 # 0
            depth = 0
            SUM = 0
            j = 2 # j - 1 # j = 0 コメントアウト
            print('s_next:{}'.format(s_next))
            print('retry_num:{}'.format(retry_num))
            
            if retry_num > 10: #20: # 40: # 追加②
                # state_history.append(s_next)
                s = s_next - 2
                # retry_num += 1

                s_next = s - 3 # 2
                depth = 0
                SUM = 0
                j = 0 # j - 1 # j = 0 コメントアウト
            elif retry_num > 5: #10: # 20: # 追加①
                # state_history.append(s_next)
                s = s_next
                # retry_num += 1

                s_next = s - 2
                depth = 0
                SUM = 0
                j = 1
            
            AAA(s_next,depth,i,j,SUM, retry_num)
            
    # if depth != 0 :
    if pi_0[s,1] == 5:
            # print('No.{} 発見 !'.format(s))


            if pi_0[s,2] == 1: # 途中
                print('No.{} 発見 !'.format(s))
                branch[j] = random.randint(1, 2)
                print("branch:{} j:{}".format(branch,j))
                Br[i] = branch
                # test = np.random.choice(List_sub, 1, p=[0.05, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.05])
                test = np.random.choice(List, 1, p=[0.20, 0.20, 0.20, 0.20, 0.20])

                TEST[i] = test  
                Diff2[i] = abs(1.0 - test)
                diff[j] = abs(1.0 - test)

                SUM += diff[j]
                state_history.append(s)
                s_next = s + 1 #+ 3
                state_history.append(s_next)
                # state_history.append(s_next)
                
                depth = 0
                AAA(s_next,depth+1,i+1,j+1,SUM, retry_num)
            else:
                print('発見 できない　!'.format(s))
                retry_num += 1
                print('depth:{}'.format(depth))
                s_next = s - depth # 3
                depth = 0
                SUM = 0
                j = 0
                state_history.append(s_next)
                AAA(s_next,depth,i,j,SUM, retry_num)


    Br[i] = branch

    
    # ここが先に s + 1 していると、s　=　1　スタートになる
    s_next = s + 1  # 上に移動するときは状態の数字が3小さくなる
    state_history.append(s_next)#(s_next)

    AAA(s_next,depth+1,i+1,j,SUM, retry_num)
    # AAA(s_next,depth,i+1,j,SUM, retry_num)
    

# 迷路内をエージェントがゴールするまで移動させる関数の定義
def AAA_top(s,depth):
    i = 0
    j = 0

    retry_num = 0

    SUM = 0
    try:
        AAA(s,depth,i,j,SUM, retry_num)
        return None
    except Exception as e:
        return e.value


def goal_maze(pi):
    s = 0  # スタート地点
    state_history = []  # 8 # エージェントの移動を記録するリスト 変更0527

    # state_history[0] = 0
    state_history.append(0) # 0527 追加
    
    state_history,SUM, retry_num = AAA_top(s,0) # s = 1
    
    return state_history,SUM, retry_num


# 迷路内をゴールを目指して、移動
state_history,SUM, retry_num = goal_maze(pi_0)

print("迷路を解くのにかかったステップ数は" + str(len(state_history) - 1) + "です")

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    
    return (line,)

# 現在地S0に緑丸を描画する
#line1, = ax.plot([1.5], [2.5], marker="*", color='y', markersize=30)
#line2, = ax.plot([1.5], [4.0], marker="d", color='r', markersize=10)

SUM_2 = np.zeros(shape=(1500))
SUM_1 = 0
SUM_3 = np.zeros(shape=(150))
j = 0
num = len(state_history) - 1
for i in range(num):  #いづれコメントアウト
    if state_history[i] == 8: # 1:
        SUM_3[j] = SUM_1
        j+=1

    Retry_sum[i] = j  # 追加 0513

    if state_history[i] == 1:
        SUM_1 = 0
    SUM_1 += Diff2[i]
    SUM_2[i] = SUM_1

    if i == len(state_history) - 2:
        SUM_2[i+1] = SUM_1
        SUM_3[j+1] = SUM_1
        Retry_sum[i+1] = retry_num

        SUM_2[i] = Diff2[i] + SUM_1

    # print("Br:{}".format(Br[i]))

# print('br:{}'.format(Br[num+1]))

    
# print('retry:{} {}'.format(Retry_sum,retry_num))
print('retry:{}'.format(retry_num-1))
# print("Br:{}".format(Br))


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    y = state  + 0.5

    z = Diff2[i]
    z += Diff2[i]

    plt.title('SUM[{:.0f}回目]={:.2f}\nbranch:{}\nΔstress={:.2f}'.format(Retry_sum[i], SUM_2[i], Br[i], Diff2[i]))
    # print("Br:{}".format(Br[i]))

    if state == 4 and pi_0[state,2] == 1:
        line1.set_data(x+0.3,y)
    elif state == 6 and pi_0[state,2] == 1:
        line2.set_data(x+0.3,y)
    elif state == 8:
        line7.set_data(x+0.3,y)
    else:
        line1.set_data(0.5,-0.5)
        line2.set_data(0.5,-0.5)
        line7.set_data(0.5,-0.5)
    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=200, repeat=False)

HTML(anim.to_jshtml())
plt.show()