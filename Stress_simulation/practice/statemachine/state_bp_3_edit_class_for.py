

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
    def __init__(self) -> None:
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



# add


if __name__ == "__main__":
    done = False

    # while not done:
    for i in range(12):

        # model.get_graph().draw(filename+'{}.png'.format(i), prog='dot', format='png') # 初期位置

        if i == 1 or i == 4:
            statemachine.UP(None)
        
        

        elif i == 2 or i == 5:
            statemachine.save_BP(None)

        elif i == 3 or i == 6:
            statemachine.RE_UP(None)
        

        elif i == 7:
            statemachine.add_stress(None)
        

        elif i == 8:
            statemachine.select_BP(None)
        

        elif i == 9:
            statemachine.DOWN(None)
        

        elif i == 10:
            statemachine.after_DOWN(None)
        

        elif i == 11:
            statemachine.BRANCH(None)

        # elif i == 8 or i == 9:
        #     break

        model.get_graph().draw(filename+'{}.png'.format(i), prog='dot', format='png') # 初期位置
        

    

    # animation()
    ims = []
    for name in os.listdir(filename):
        _, ext = os.path.splitext(name)
        if ext == '.png':
            ims.append(imageio.imread(filename + name))
            
    imageio.mimwrite('anim_mdp8.gif', ims, fps = 0.8)


    print([event for event in machine.events])