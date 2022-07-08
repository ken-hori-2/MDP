import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/


class Anim():
    # def __init__(self, STATE_HISTORY):
    def __init__(self):
        # self.state_history = [0,1,2]
        self.state_history = [[11], [10], [9], [8], [9], [10], [11], [12]]
        # self.state_history = [[0], [1], [2], [1], [0], [1], [2], [0]]
        # self.state_history = STATE_HISTORY
        # print("STATE_HISTORY:{}".format(STATE_HISTORY))
        arr = np.array(self.state_history)
        self.state_history = arr.flatten()
        print("STATE_HISTORY:{}".format(self.state_history))

        self.data_change()

        self.fig = plt.figure(figsize=(3, 5))
        self.ax = plt.gca()
        self.ims = []

        self.view_plot_text()
        self.move_history()
        self.view_anim()

    def data_change(self): # ここを別のリストに入れてみる
        for i in range(len(self.state_history)):
            if self.state_history[i] == 11:
                self.state_history[i] = 0
            elif self.state_history[i] == 12:
                self.state_history[i] = -1
            elif self.state_history[i] == 10:
                self.state_history[i] = 1
            elif self.state_history[i] == 9:
                self.state_history[i] = 2
            elif self.state_history[i] == 8:
                self.state_history[i] = 1
            print("Data Change !!")

        # return


    def view_plot_text(self):
        # 状態を示す文字S0～S8を描く
        plt.text(0.2, 1.5, 'S0', size=10, ha='center')
        plt.text(0.2, 3.5, 'S1', size=10, ha='center')
        plt.text(0.2, 5.5, 'S2', size=10, ha='center')
        plt.text(0.8, 1.5, 'Branch', size=10, ha='center')
        plt.plot([0.5, 0.5], [1.5, 5.5], color="black")
        # plt.plot([0.5], [1.5], marker="s", color='black', markersize=40)
        # plt.plot([0.5], [3.5], marker="s", color='black', markersize=40)
        # plt.plot([0.5], [5.5], marker="s", color='black', markersize=40)
        plt.plot([0.5], [1.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [3.5], marker="s", color='grey', markersize=40)
        plt.plot([0.5], [5.5], marker="s", color='grey', markersize=40)
        plt.plot([0.8], [1.5], marker="s", color='grey', markersize=40)

        # 描画範囲の設定と目盛りを消す設定
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 7)
        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')
        
        
    
    def move_history(self):
        line, = plt.plot([], [])
        self.ims.append([line])

        for t in range(len(self.state_history)): # フレームごとの描画内容
            
            state = self.state_history[t]  # 現在の場所を描く

            if state == -1:
                print("分岐")
                x = 0.8
                y = 1.5
                # line, = plt.plot(x, y, marker="o", color='y', markersize=20)
            else:
                x = 0.5
                y = state + (state) + 1.5

            # line, = plt.plot(x, y, marker="o", color='g', markersize=20)
            line, = plt.plot(x, y, marker="s", color='r', markersize=40, alpha = 0.5)
            self.ims.append([line])
            if t == 0:
                self.ims.append([line])



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=1000, repeat = False)
        plt.show()
        return True


if __name__ == "__main__":
    Anim()