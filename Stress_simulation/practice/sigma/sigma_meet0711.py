
import numpy as np

from statistics import mean, median,variance,stdev

from sympy import N



def main():


    data = [1.1, 1.2, 1.0, 1.1]
    data = [1.1, 1.2, 1.0, 1.1]
    N = 0
    
    mu_list = np.zeros(shape=len(data))
    std_list = np.zeros(shape=len(data))
    for i in range(len(data)):
        
        if i == 0:
            std = 0.0
        else:
            std = stdev(data)
        
            mu = mean(data)
            
            
            print("\ndata:{}".format(data))
            # print(" mu:{}".format(mu))
            print(" std:{:.2f}".format(std))
            mu_list[i] = mu
            std_list[i] = std

            n = 1.0 - std
            N += n
            print(" 納得度 n :{}".format(n))
            print(" 納得度の総和 N :{}".format(N))

    print("\nsigma:{}".format(std_list))



if __name__ == "__main__":
    main()