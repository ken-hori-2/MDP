import matplotlib.pyplot as plt
import numpy as np

# from mdp import main

# 結果グラフで描写
class Illustration():

    def __init__(self, IGNITIONLIST, TOTALREWARD_LIST):
        self.IGNITIONLIST = IGNITIONLIST
        self.fig = plt.figure(figsize=(5, 5))
        self.length = len(self.IGNITIONLIST)
        self.x_plot = np.arange(1, self.length+1, 1)
        
        self.x = np.arange(0, 101, 1)
        self.y = TOTALREWARD_LIST

        self.view_bar()
        self.view_plot()

    def view_bar(self):
        

        plt.title("Graph of IGNITION locations")
        plt.xlabel("Number of retries")
        # plt.ylabel("Ignited NODE Location")
        plt.ylabel("Stress at the moment of ignition")
        plt.xlim(0, self.length)
        plt.bar(self.x_plot, self.IGNITIONLIST, label = "IGNITION location", color="orange", ec="black")
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
        plt.xlim(-1, 101)
        plt.legend()
        plt.grid()
        plt.show()

        return True