from transitions.extensions import GraphMachine
states = ['A', 'B', 'C']    #状態の定義

class Matter(object):
    pass

model = Matter()
machine = GraphMachine(model=model, states=states, initial=states[0], 
                       auto_transitions=False, ordered_transitions=True,
                       title="", show_auto_transitions=True, show_conditions=True)



filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test_2.png'
model.get_graph().draw(filename, prog='dot', format='png')
# import io
# from IPython.display import Image, display

# stream = io.BytesIO()
# model.get_graph().draw(stream, prog='dot', format='png')
# display(Image(stream.getvalue()))



print(model.is_A())
print(model.is_B())



print(machine.set_state('B'))
print(model.state)
print(model.is_B())
