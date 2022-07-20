
from statistics import mean, median,variance,stdev

# data = [1.0, 1.1, 1.2]
# # data = [100, 120]

# m = mean(data)
# median = median(data)
# variance = variance(data)
# stdev = stdev(data)
# print('平均: {0:.2f}'.format(m))
# # print('中央値: {0:.2f}'.format(median))
# print('分散: {0:.2f}'.format(variance))
# print('標準偏差: {0:.2f}'.format(stdev))








# ガウス関数を定義
def gauss(x, a=1, mu=0, sigma=1):
    return a * np.exp(-(x - mu)**2 / (2*sigma**2))

def view(data, ave, std):

    # -4～8まで0.1刻みの数値の配列
    x = np.arange(0.5, 1.5, 0.1)
    # f2 = gauss(x, a=0.5, mu=0.5, sigma=2)
    f2 = gauss(x, mu=ave, sigma=std)
    plt.plot(x, f2, color="blue", label="μ={:.3f}, σ={:.3f}".format(ave, std))
    plt.legend()
    plt.grid()
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def anim(mu_list, std_list):
    fig = plt.figure()

    ims = []

    x = np.arange(0.5, 2.0, 0.01)
    for i in range(3):
            # rand = np.random.randn(100)     # 100個の乱数を生成
            mu = mu_list[i]
            std = std_list[i]
            f2 = gauss(x, mu=mu, sigma=std)
            im = plt.plot(x, f2, color="blue", label="μ={:.3f}, σ={:.3f}".format(mu, std))
            ims.append(im)                  # グラフを配列 ims に追加

    # 10枚のプロットを 100ms ごとに表示
    ani = animation.ArtistAnimation(fig, ims, interval=500)
    plt.show()


if __name__ == '__main__':


    data = []
    
    mu_list = np.zeros(shape=3)
    std_list = np.zeros(shape=3)
    for i in range(3):
        
        if i == 0:
            data.append(1.0)
            std = 0.0
        elif i == 1:
            data.append(1.1)
            # variance = variance(data)
            std = stdev(data)
        elif i == 2:
            data.append(1.2)
            # variance = variance(data)
            std = stdev(data)
        
        mu = mean(data)
        
        
        print("\ndata:{}".format(data))
        print(" mu:{}".format(mu))
        print(" std:{:.2f}".format(std))
        mu_list[i] = mu
        std_list[i] = std


        # view(data, mu, std)

        N = 1.0 - std
        print(" 納得度N:{}".format(N))

    print("\nsigma:{}".format(std_list))


    # anim(mu_list, std_list)