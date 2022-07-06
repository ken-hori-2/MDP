
#numpy,scipy.statsからnorm,math,matplotlib.pyplotをインポート！
import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt

#0から100まで、0.01間隔で入ったリストXを作る！
# X = np.arange(0,100,0.1)
fig = plt.figure(figsize=(5, 5))
X = np.arange(0,5,1)
#確率密度関数にX,平均50、標準偏差20を代入
# Y = norm.pdf(X,50,20)
# Y = 0.1, 0.21, 0.331, 0.4641, 0.61051#-X+4 #2*X # norm.pdf(X,0.5,0.1)
# Y = 0.1, 0.22, 0.364, 0.5368, 0.74416
Y = 0.1, 0.21, 0.131, 0.2441, 0.16851
# Y = 0.1 + 1.1*(X)
#x,yを引数にして、関数の色をr(red)に指定！カラーコードでも大丈夫です！
plt.plot(X,Y,color='orange')
plt.grid()
plt.show()