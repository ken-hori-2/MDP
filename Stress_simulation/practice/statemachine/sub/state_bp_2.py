import io
from IPython.display import Image, display
from transitions.extensions import GraphMachine

states = ['Go', 
          'Δs max', 
          'BP decision', 
          'Down', 
          'Branch']        #状態の定義

class Matter(object):
    
    pass


model = Matter()                #ファイル出力する場合は、Matter('test.png')にする。
machine = GraphMachine(model=model, states=states, initial=states[0], 
                       auto_transitions=False, ordered_transitions=True,
                       show_auto_transitions=False, show_conditions=False)    


# model.action_output_graph()     #初回のみ手動実施
filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/gif_fig/4.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/gif_fig/3.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/gif_fig/2.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/gif_fig/1.png'
model.get_graph().draw(filename, prog='dot', format='png')

model.next_state()

filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/gif_fig/0.png'
model.get_graph().draw(filename, prog='dot', format='png')