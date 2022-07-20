
from re import A
import numpy as np
from math import fabs
from transitions.extensions import GraphMachine
import matplotlib.pyplot as plt
from matplotlib import animation
import imageio
import os

states = ['Go',
          'Storage',
          'Δs max', 
          'BP decision', 
          'Down', 
          'Branch',
          'Add Down',
          'Exp range'
          ]        #状態の定義


transitions = [
               {'trigger':'継続', 'source':'Go', 'dest':'Go'},
               {'trigger':'BP候補保存', 'source':'Go', 'dest':'Storage'},
               {'trigger':'再継続', 'source':'Storage', 'dest':'Go'},

               {'trigger':'ストレスの蓄積', 'source':'Go', 'dest':'Δs max'},
               {'trigger':'戻る位置の決定', 'source':'Δs max', 'dest':'BP decision'},
               {'trigger':'戻る', 'source':'BP decision', 'dest':'Down'},   
               {'trigger':'戻った後の行動決定_真', 'source':'Down', 'dest':'Branch'},
               {'trigger':'別の道を探索', 'source':'Branch', 'dest':'Go'},
               {'trigger':'さらに戻る_偽', 'source':'Down', 'dest':'Add Down'},
               {'trigger':'戻る位置の決定', 'source':'Add Down', 'dest':'BP decision'},
               {'trigger':'探索範囲の拡大', 'source':'Down', 'dest':'Exp range'},
               {'trigger':'より広く探索', 'source':'Exp range', 'dest':'Go'}    
              ]

class Model(object):
    pass

model = Model()
machine = GraphMachine(model=model, states=states, transitions=transitions, initial=states[0], 
                       auto_transitions=False, ordered_transitions=False, title='',
                       show_auto_transitions=True)

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class_for/'



class statemachine():

    def __init__(self):
        
        pass

    def save_BP(self):
        model.BP候補保存()
    
    def UP(self):
        model.継続()

    def RE_UP(self):
        model.再継続()

    def add_stress(self):
        model.ストレスの蓄積()

    def select_BP(self):
        model.戻る位置の決定()

    def DOWN(self):
        model.戻る()

    def after_DOWN(self):
        model.戻った後の行動決定_真()

    def BRANCH(self):
        model.別の道を探索()

class animation():
    def __init__(self):
        self.ims = []
        self.filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class_for/'
        self.draw()

    def draw(self):
        for name in os.listdir(self.filename):
            _, ext = os.path.splitext(name)
        if ext == '.png':
            self.ims.append(imageio.imread(self.filename + name))
            
        imageio.mimwrite('anim_mdp9.gif', self.ims, fps = 0.8)



class algorithm():

    def __init__(self, s, stressfull):
        # model.get_graph().draw(filename+'{}.png'.format(i), prog='dot', format='png') # 初期位置
        self.s = s
        self.max = stressfull
        self.trigar = False
        self.select = False
        self.bp = False
        self.down = False
        self.branch = False
        self.save = False
        self.BPLIST = []
        # self.NODELIST = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.NODELIST = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # print("stress:{}".format(self.s))
        self.A = False
        self.next_bp = 0
    
    def model(self, a, done, i):
        
        
        if self.s < self.max:
            print("stress:{}".format(self.s))
            if self.NODELIST[i] == 1 and not self.save: # and self.NODELIST[count+1] == 0:
                self.BPLIST.append(i)
                # 一個前が1ならpopで削除
                print("削除前 {}".format(self.BPLIST))
                # if i > 0:
                if self.NODELIST[i - 1] == 1: #  and i != 1:
                    self.BPLIST.pop(-2)
                    print("削除後 {}".format(self.BPLIST))
                # self.BPLIST.append(i)
                print("storage  BPLIST:{}".format(self.BPLIST))
                self.save = True
                statemachine.save_BP(None)
                return done, i

            if self.save:
                self.save = False
                statemachine.RE_UP(None)
                # return done, i



            i += 1
            statemachine.UP(None)
            # return done, i
            if self.NODELIST[i] == 0:    
                self.s += a
                
            return done, i
        

        if self.s >= self.max and not self.trigar:
            self.trigar = True
            self.select = True
            print("stressfull")
            statemachine.add_stress(None)
            return done, i
        

        if self.select:
            self.select = False
            self.bp = True
            print("bp")
            self.next_bp = self.BPLIST[-1]
            print("[next bp : {}]".format(self.next_bp))
            statemachine.select_BP(None)
            return done, i
        

        if self.bp:
            self.bp = False
            self.down  = True
            print("down")
            a = True
            while a:
                i -= 1
                if i == self.next_bp:
                    a = False
            statemachine.DOWN(None)
            return done, i
        

        if self.down:
            self.down = False
            self.branch = True
            print("afterdown decision")
            statemachine.after_DOWN(None)
            return done, i
        

        if self.branch:
            self.branch = False
            print("branch")
            done = True
            statemachine.BRANCH(None)
            return done, i



# add


if __name__ == "__main__":
    done = False
    s = 0
    stressfull = 5
    a = 1

    algo = algorithm(s, stressfull)
    # for i in range(20):
    count = 0
    i = 0
    while not done:
        print("{} NODE {}".format(count, i))
        
        done , i = algo.model(a, done, i)

        print("⇩")

        count += 1

        

        model.get_graph().draw(filename+'{}.png'.format(count), prog='dot', format='png') # 初期位置
        

    

    # animation()
    ims = []
    for name in os.listdir(filename):
        _, ext = os.path.splitext(name)
        if ext == '.png':
            ims.append(imageio.imread(filename + name))
            
    imageio.mimwrite('anim_mdp8.gif', ims, fps = 0.8)


    print([event for event in machine.events])