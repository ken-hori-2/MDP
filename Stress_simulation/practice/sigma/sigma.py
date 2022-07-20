
import numpy as np

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


def main():


    data = []
    N = 0
    
    mu_list = np.zeros(shape=4)
    std_list = np.zeros(shape=4)
    for i in range(4):
        
        if i == 0:
            data.append(1.0)
            std = 0.0
            continue
        elif i == 1:
            data.append(1.1)
            std = stdev(data)
        elif i == 2:
            data.append(1.2)
            std = stdev(data)
        elif i == 3:
            data.append(1.3)
            std = stdev(data)
        
        mu = mean(data)
        
        
        print("\ndata:{}".format(data))
        # print(" mu:{}".format(mu))
        print(" std:{:.2f}".format(std))
        mu_list[i] = mu
        std_list[i] = std

        n = 1.0 - std
        print(" 納得度N:{}".format(n))
        N += n
        print(" 納得度の総和 N :{}".format(N))
        if N >= 1.0:
            print("終了")
            break

    print("\nsigma:{}".format(std_list))



if __name__ == "__main__":
    main()