#動作する最小構成のステートマシンの定義
from transitions import Machine
states=['A', 'B', 'C']    #状態の定義

class Matter(object):
    pass

model = Matter()
machine = Machine(model=model, states=states, initial='A', 
                  auto_transitions=False, ordered_transitions=True)


print(model.state)

print(model.next_state())

print(model.state)

print(model.next_state())

print(model.state)