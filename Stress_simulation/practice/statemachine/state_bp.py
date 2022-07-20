import io
from IPython.display import Image, display
from transitions.extensions import GraphMachine

states = ['A', 'B', 'C']        #状態の定義

class Matter(object):
    
    pass


model = Matter()                #ファイル出力する場合は、Matter('test.png')にする。
machine = GraphMachine(model=model, states=states, initial='A', 
                       auto_transitions=False, ordered_transitions=True,
                       show_auto_transitions=False, show_conditions=False)    


# model.action_output_graph()     #初回のみ手動実施
filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test1.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test2.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test3.png'
model.get_graph().draw(filename, prog='dot', format='png')