from transitions import Machine
from transitions.extensions import GraphMachine

states = ['A', 'B', 'C']    #状態の定義

class Model(object):
    pass

model = Model()
machine = GraphMachine(model=model, states=states, initial=states[0], 
                  auto_transitions=False, ordered_transitions=True,
                  title="", show_auto_transitions=True, show_conditions=True)



filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test_s6.png'
model.get_graph().draw(filename, prog='dot', format='png')