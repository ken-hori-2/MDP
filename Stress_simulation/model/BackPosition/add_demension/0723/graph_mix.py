import matplotlib.pyplot as plt
import numpy as np

# from mdp import main

# 結果グラフで描写
class Illustration():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.fig = plt.figure(figsize=(5, 5))
        self.length = len(self.a)
        self.x_plot = np.arange(1, self.length+1, 1)
        # self.x_plot = np.arange(1, 11, 1)
        
        # self.x = np.arange(0, 101, 1)
        # self.x = np.arange(0, 50, 1)
        # self.y = TOTALREWARD_LIST

        self.view_bar()
        # self.view_plot()

    def view_bar(self):
        

        plt.title("Graph of Back Position")
        plt.xlabel("Number of steps")
        # plt.ylabel("Ignited NODE Location")
        plt.ylabel("State (Node)")
        plt.xlim(-5, self.length+10)
        # plt.bar(self.x_plot, self.a, label = "IGNITION location", color="orange", ec="black")
        plt.plot(self.x_plot, self.a, label = "Agent Position", color="orange", marker = "^", markersize = 5, alpha = 0.8)
        plt.plot(self.x_plot, self.b, label = "Agent Position", color="blue", marker = "s", markersize = 5, alpha = 0.5)
        plt.plot(self.x_plot, self.c, label = "Agent Position", color="red", marker = "D", markersize = 5, alpha = 0.5)
        # plt.hlines(IGINITION_AVE, 1, X, color="orange", linewidth = 3, label="average")
        plt.legend()
        plt.grid()
        plt.show()
        
        return True

    def view_plot(self):
        plt.title("Graph of IGNITION locations")
        plt.xlabel("Number of steps")
        plt.ylabel("Total stress")
        plt.plot(self.x, self.y, label = "Stress and number of steps", color="orange")
        # plt.xlim(-1, 101)
        plt.legend()
        plt.grid()
        plt.show()

        return True





if __name__ == "__main__":

    # state_history_a = [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1, 0, 0, 1, 1, 2]
    state_history_a = [0, 0, 1, 1, 2, 3, 3, 4, 5, 5, 5, 3, 3, 3, 1, 1]

    # state_history_b = [0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1, 0, 0]
    state_history_b = [0, 0, 1, 1, 2, 3, 4, 4, 4, 1, 1  ,1,1,1,1,1]

    # state_history_c = [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2, 0, 0, 1, 1, 2, 2, 3, 4, 5, 5]
    state_history_c = [0, 0, 1, 1, 2, 2, 3, 4, 5, 5, 5, 2, 2  ,1,1,1]
    Illustration(state_history_a, state_history_b, state_history_c)