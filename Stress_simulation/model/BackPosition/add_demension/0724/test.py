import numpy as np
# 行は状態0～7、列は移動方向で↓、→、↑、←を表す
theta_0 = np.array([[np.nan, 1, 1, np.nan],  # s0
                    [np.nan, 1, np.nan, 1],  # s1
                    [np.nan, np.nan, 1, 1],  # s2
                    [1, 1, 1, np.nan],  # s3
                    [np.nan, np.nan, 1, 1],  # s4
                    [1, np.nan, np.nan, np.nan],  # s5
                    [1, np.nan, np.nan, np.nan],  # s6
                    [1, 1, np.nan, np.nan],  # s7、※s8はゴールなので、方策はなし
                    ])
def simple_convert_into_pi_from_theta(theta):
    '''単純に割合を計算する'''
    [m, n] = theta.shape
    pi = np.zeros((m, n))
    for i in range(0, m):
        pi[i, :] = theta[i, :] / np.nansum(theta[i, :])
    pi = np.nan_to_num(pi)
    return pi
# 初期の方策pi_0を求める
pi_0 = simple_convert_into_pi_from_theta(theta_0)
direction = ["down", "right", "up", "left"]
width = 3
height = 3
max_state = width * height - 1
agent_Q = np.random.rand(max_state, 4) * theta_0 # 初期の価値観数
# eta = 0.1  # 学習率
# gamma = 0.9  # 時間割引率
# epsilon = 0.5 #ε-greedy

print(agent_Q)