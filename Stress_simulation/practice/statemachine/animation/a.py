from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def plot(img_path):
    # 前のフレームの描画をクリアする。
    ax.cla()
    img = plt.imread(img_path)
    ax.imshow(img)
    ax.set_axis_off()


img_dir = Path("/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/fig")
img_paths = img_dir.glob("*.jpg")

# アニメーションを作成する。
fig, ax = plt.subplots()
anim = FuncAnimation(fig, plot, frames=img_paths, interval=300)
plt.show()

# gif 画像として保存する。
anim.save("animation5.gif", writer="pillow")
plt.show()