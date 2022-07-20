

from transitions.extensions import GraphMachine

states = ['Go',
          'Storage',
          'Δs max', 
          'BP decision', 
          'Down', 
          'Branch',
          'Add Down',
          'Exp range']        #状態の定義


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
                       show_auto_transitions=True)                  # 当行を追加

# filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class/trans_'
filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class/'
model.get_graph().draw(filename+'7.png', prog='dot', format='png') # ファイルで出力





# add
import matplotlib.pyplot as plt
from matplotlib import animation
import imageio
import os

if __name__ == "__main__":
    ims = []
    # fig = plt.figure(figsize=(5, 3))

    model.BP候補保存()
    model.get_graph().draw(filename+'6.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'6.png', prog='dot', format='png')) # ファイルで出力

    model.継続()
    model.get_graph().draw(filename+'5.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'5.png', prog='dot', format='png')) # ファイルで出力

    model.ストレスの蓄積()
    model.get_graph().draw(filename+'4.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'4.png', prog='dot', format='png')) # ファイルで出力

    model.戻る位置の決定()
    model.get_graph().draw(filename+'3.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'3.png', prog='dot', format='png')) # ファイルで出力

    model.戻る()
    model.get_graph().draw(filename+'2.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'2.png', prog='dot', format='png')) # ファイルで出力

    model.戻った後の行動決定_真()
    model.get_graph().draw(filename+'1.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'1.png', prog='dot', format='png')) # ファイルで出力

    model.別の道を探索()
    model.get_graph().draw(filename+'0.png', prog='dot', format='png')
    # ims.append(model.get_graph().draw(filename+'0.png', prog='dot', format='png')) # ファイルで出力

    # filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class/'

    for name in os.listdir(filename):
        _, ext = os.path.splitext(name)
        if ext == '.png':
            ims.append(imageio.imread(filename + name))
            
    imageio.mimwrite('anim_mdp8.gif', ims, fps = 0.8)

    # print(ims)
    # anim = animation.ArtistAnimation(fig, ims, interval=500)

    # anim = imageio.mimwrite(ims, interval=500)
    # plt.show()


    print([event for event in machine.events])