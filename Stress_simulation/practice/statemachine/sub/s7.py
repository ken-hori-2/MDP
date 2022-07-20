# from transitions import Machine

# states = ['A', 'B', 'C']    #状態の定義
# transitions = [
#     {'trigger':'fromAtoB', 'source':'A', 'dest':'B'},
#     {'trigger':'fromBtoC', 'source':'B', 'dest':'C'},
#     {'trigger':'fromCtoA', 'source':'C', 'dest':'A'},   
# ]
# class Model(object):
#     pass

# model = Model()
# machine = Machine(model=model, states=states, transitions=transitions, initial=states[0],  
#                   auto_transitions=True, ordered_transitions=True)
# machine.add_ordered_transitions(states=['A', 'B', 'C']) #順序遷移の付与



# print([event for event in machine.events])

from transitions.extensions import GraphMachine

states = ['A', 'B', 'C']    # 状態の定義

transitions = [
    {'trigger':'fromAtoB', 'source':'A', 'dest':'B'},
    {'trigger':'fromBtoC', 'source':'B', 'dest':'C'},
    {'trigger':'fromCtoA', 'source':'C', 'dest':'A'},   
    # {'trigger':'toB', 'source':'A', 'dest':'B'},
    # {'trigger':'toC', 'source':'B', 'dest':'C'},
    # {'trigger':'toA', 'source':'C', 'dest':'A'},   
]

class Model(object):
    pass

model = Model()
machine = GraphMachine(model=model, states=states, transitions=transitions, initial=states[0], 
                       auto_transitions=True, ordered_transitions=False, title='',
                       show_auto_transitions=True)                  # 当行を追加
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/transitions_1.png', prog='dot', format='png') # ファイルで出力

# print([event for event in machine.events])
model.fromAtoB()
# model.toB()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/transitions_2.png', prog='dot', format='png') # ファイルで出力

model.fromBtoC()
# model.toC()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/transitions_3.png', prog='dot', format='png') # ファイルで出力

model.fromCtoA()
# model.toA()
model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/transitions_4.png', prog='dot', format='png') # ファイルで出力

# model.toC()
# model.get_graph().draw('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/transitions.png', prog='dot', format='png') # ファイルで出力