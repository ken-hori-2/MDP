

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
               {'trigger':'継続', 'source':'Storage', 'dest':'Go'},
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

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class/'



class statemachine():
    def __init__(self) -> None:
        pass

    def save_BP(self):
        model.BP候補保存()
    
    def UP(self):
        model.継続()

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
        self.filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class/'
        self.draw()

    def draw(self):
        for name in os.listdir(self.filename):
            _, ext = os.path.splitext(name)
        if ext == '.png':
            self.ims.append(imageio.imread(self.filename + name))
            
        imageio.mimwrite('anim_mdp8.gif', self.ims, fps = 0.8)



# add


if __name__ == "__main__":
    
    

    model.get_graph().draw(filename+'0.png', prog='dot', format='png') # 初期位置

    # model.BP候補保存()
    statemachine.save_BP(None)
    model.get_graph().draw(filename+'1.png', prog='dot', format='png')

    # model.継続()
    statemachine.UP(None)
    model.get_graph().draw(filename+'2.png', prog='dot', format='png')

    # model.ストレスの蓄積()
    statemachine.add_stress(None)
    model.get_graph().draw(filename+'3.png', prog='dot', format='png')

    # model.戻る位置の決定()
    statemachine.select_BP(None)
    model.get_graph().draw(filename+'4.png', prog='dot', format='png')

    # model.戻る()
    statemachine.DOWN(None)
    model.get_graph().draw(filename+'5.png', prog='dot', format='png')

    # model.戻った後の行動決定_真()
    statemachine.after_DOWN(None)
    model.get_graph().draw(filename+'6.png', prog='dot', format='png')

    # model.別の道を探索()
    statemachine.BRANCH(None)
    model.get_graph().draw(filename+'7.png', prog='dot', format='png')

    

    animation()


    print([event for event in machine.events])