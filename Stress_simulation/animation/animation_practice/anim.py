import matplotlib.pyplot as plt


state_history = [0,1,2]


fig = plt.figure(figsize=(3, 5))
ax = plt.gca()

# 状態を示す文字S0～S8を描く
plt.text(0.2, 1.5, 'S0', size=10, ha='center')
plt.text(0.2, 3.5, 'S1', size=10, ha='center')
plt.text(0.2, 5.5, 'S2', size=10, ha='center')

# plt.plot([0.5, 0.5], [0.0, 8.5],color="black")

# 描画範囲の設定と目盛りを消す設定
ax.set_xlim(0, 1)
ax.set_ylim(0, 7)
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='off', right='off', left='off', labelleft='off')

ax.plot([0.5], [1.5], marker="s", color='black', markersize=40)
ax.plot([0.5], [3.5], marker="s", color='black', markersize=40)
ax.plot([0.5], [5.5], marker="s", color='black', markersize=40)

# 現在地S0に緑丸を描画する
line, = ax.plot([0.5], [1.5], marker="o", color='g', markersize=20)

# エージェントの移動の様子を可視化します
# 参考URL http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
from matplotlib import animation
from IPython.display import HTML
import matplotlib.cm as cm  # color map


def init():
    '''背景画像の初期化'''
    line.set_data([], [])
    
    return (line,)


def animate(i):
    '''フレームごとの描画内容'''
    state = state_history[i]  # 現在の場所を描く
    x = 0.5  # 状態のx座標は、3で割った余り+0.5
    # y = state  + 1.5
    y = state + (state) + 1.5

    line.set_data(x, y)
    return (line,)


#　初期化関数とフレームごとの描画関数を用いて動画を作成する
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(
    state_history), interval=800, repeat=False)

HTML(anim.to_jshtml())
plt.show()