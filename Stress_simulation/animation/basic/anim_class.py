from cv2 import repeat
import matplotlib.pyplot as plt

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML




class Anim():
    def __init__(self):
        self.state_history = [0,1,2]
        self.fig = plt.figure(figsize=(3, 5))
        self.ax = plt.gca()
        self.ims = []

        self.view_plot_text()
        self.move_history()
        self.view_anim()

    def view_plot_text(self):
        # 状態を示す文字S0～S8を描く
        plt.text(0.2, 1.5, 'S0', size=10, ha='center')
        plt.text(0.2, 3.5, 'S1', size=10, ha='center')
        plt.text(0.2, 5.5, 'S2', size=10, ha='center')
        plt.plot([0.5, 0.5], [1.5, 5.5],color="black")

        # 描画範囲の設定と目盛りを消す設定
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 7)
        plt.tick_params(axis='both', which='both', bottom='off', top='off',
                        labelbottom='off', right='off', left='off', labelleft='off')

        self.ax.plot([0.5], [1.5], marker="s", color='black', markersize=40)
        self.ax.plot([0.5], [3.5], marker="s", color='black', markersize=40)
        self.ax.plot([0.5], [5.5], marker="s", color='black', markersize=40)
        
        
    
    def move_history(self):
        line, = self.ax.plot([], [])
        self.ims.append([line])

        for t in range(len(self.state_history)): # フレームごとの描画内容
            
            state = self.state_history[t]  # 現在の場所を描く
            x = 0.5
            y = state + (state) + 1.5
            
            line, = self.ax.plot(x, y, marker="o", color='g', markersize=20)
            self.ims.append([line])
            if t == 0:
                self.ims.append([line])



    def view_anim(self): #　初期化関数とフレームごとの描画関数を用いて動画を作成する
        self.anim = animation.ArtistAnimation(self.fig, self.ims, interval=800, repeat = False)
        plt.show()


Anim()