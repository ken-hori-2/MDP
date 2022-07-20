from transitions.extensions import GraphMachine

states = ['A', 'B', 'C']    # 状態の定義

class Model(object):
    pass

model = Model()
machine = GraphMachine(model=model, states=states, initial=states[0], 
                       auto_transitions=True, ordered_transitions=False, title='',
                       show_auto_transitions=True)                  # 当行を追加
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/t_1.png', prog='dot', format='png') # ファイルで出力

# print([event for event in machine.events])
model.fromAtoB()
# model.toB()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/t_2.png', prog='dot', format='png') # ファイルで出力

model.fromBtoC()
# model.toC()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/t_3.png', prog='dot', format='png') # ファイルで出力

model.fromCtoA()
# model.toA()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/t_4.png', prog='dot', format='png') # ファイルで出力