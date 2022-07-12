
import numpy as np
import matplotlib.pyplot as plt

from statistics import mean, median,variance,stdev




def main():


    data = []
    N = 0
    n = 0
    num = 4
    N_list = np.zeros(shape=num)
    
    mu_list = np.zeros(shape=num)
    std_list = np.zeros(shape=num)
    for i in range(num):
        
        if i == 0:
            # data.append(1.1)
            data.append(1.6)
            std = 0.0
            continue
        elif i == 1:
            # data.append(1.2)
            data.append(0.5)
            std = stdev(data)
        elif i == 2:
            # data.append(1.0)
            data.append(1.7)
            std = stdev(data)
        elif i == 3:
            # data.append(1.3)
            data.append(0.8)
            std = stdev(data)
        
        mu = mean(data)
        
        print("retry:{}".format(i))
        print("\ndata:{}".format(data))
        # print(" mu:{}".format(mu))
        print(" std:{:.2f}".format(std))
        mu_list[i] = mu
        std_list[i] = std

        n = 1.0 - std
        print(" 納得度N:{}".format(n))
        N += n
        N_list[i] = N
        print(" 納得度の総和 N :{}".format(N))


        # x = np.arange(1, 5, 1)
        x = np.arange(0, 4, 1)
        # y = N
        plt.title("納得度の推移")
        plt.xlabel("リトライ数")
        plt.ylabel("納得度の総和")
        plt.ylim(0, 2)
        plt.axhline(y=1, xmin=0, xmax=5)
        plt.bar(x, N_list, label = "納得度", color="orange", ec="black")
        plt.legend()
        plt.grid()
        # plt.show()


        if N >= 1.0:
            print("終了")
            break

        

    print("\nsigma:{}".format(std_list))
    plt.show()



if __name__ == "__main__":
    main()