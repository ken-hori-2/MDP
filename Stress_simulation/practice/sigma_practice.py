import matplotlib.pyplot as plt
import numpy as np

def calculate_mean(data):
    s = sum(data)
    N = len(data)
    mean =s/N

    return mean

#平均からの偏差を求める
def find_difference(data):
    mean = calculate_mean(data)
    diff = []

    for num in data:
        diff.append(num-mean)
    return diff

def calculate_variance(data):
    diff = find_difference(data)
    #差の２乗を求める
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)

    #分散を求める
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(data)
    return variance

# ガウス関数を定義
def gauss(x, a=1, mu=0, sigma=1):
    return a * np.exp(-(x - mu)**2 / (2*sigma**2))

def view(data, ave, std):
    # # x = np.arange(0, len(data), 1)
    # x = np.arange(0, 1, 0.1)
    # plt.title("Graph of IGNITION locations")
    # plt.xlabel("Number of steps")
    # plt.ylabel("Total stress")
    # plt.plot(x, data, marker = "o", label = "sigma practice", color="orange", linestyle = ":")
    # # plt.xlim(-1, 101)
    # # 散布図を表示
    # # 乱数を data数分生成
    # value = np.random.rand(len(data))
    # plt.scatter(x, data, s=100, c=value)
    # # plt.scatter(x, data)
    # # plt.plot(x, data, marker = "-", label = "sigma practice", color="orange")

    
    
    # # カラーバーを表示
    # plt.colorbar()
    # plt.legend()
    # plt.grid()
    # plt.show()

    # -4～8まで0.1刻みの数値の配列
    x = np.arange(0.0, 1.1, 0.1)
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

    # data_list = np.zeros(shape=3)
    # data_list[0] = (0.5,0.6,0.7,0.8)
    # data_list[1] = (0.6,0.7,0.8,0.8)
    # data_list[2] = (0.7,0.8,0.8,0.8)
    x = np.arange(0.0, 1.1, 0.01)
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
    # data = [100,200,300,400,500,500,600,700,800,800]
    # data = [0.1,0.2,0.3,0.4,0.5,0.5,0.6,0.7,0.8,0.8]
    data0 = [0.5,0.6,0.7,0.8]
    data1 = [0.6,0.7,0.8,0.8]
    data2 = [0.7,0.8,0.8,0.8]
    # data = [0.8,0.8,0.8,0.8]

    mu_list = np.zeros(shape=3)
    std_list = np.zeros(shape=3)
    for i in range(3):
        # data = exec("data" + str(i))
        # data = ("data{}".format(i))
        if i == 0:
            mu = sum(data0) / len(data0)
            variance = calculate_variance(data0)
            print('分散の値は:{0}'.format(variance))

            std = variance**0.5
            print('標準偏差は:{0}'.format(std))
        elif i == 1:
            mu = sum(data1) / len(data1)
            variance = calculate_variance(data1)
            print('分散の値は:{0}'.format(variance))

            std = variance**0.5
            print('標準偏差は:{0}'.format(std))
        elif i == 2:
            mu = sum(data2) / len(data2)
            variance = calculate_variance(data2)
            print('分散の値は:{0}'.format(variance))

            std = variance**0.5
            print('標準偏差は:{0}'.format(std))


        mu_list[i] = mu
        std_list[i] = std

    # view(data, mu, std)


    anim(mu_list, std_list)