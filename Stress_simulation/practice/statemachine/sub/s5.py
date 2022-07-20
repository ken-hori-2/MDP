from transitions import Machine
from transitions.extensions.states import add_state_features, Error

from transitions.extensions import GraphMachine
states = ['A', 'B', 'C']    #状態の定義

@add_state_features(Error)
class CustomMachine(Machine):
    pass

# 状態の定義(終端状態例外、タグ機能付き)
states = ['start', 'processing',                                # (遷移のある状態なので例外発生なし)
          'error',                                              # 終端状態例外あり
          {'name':'warn', 'accepted':True},                     # 終端状態例外なし
          {'name':'exit', 'tags':['accepted', 'Compleat']}]     # 終端状態例外なし+Compleatタグ

# 遷移の定義
transitions = [ 
    {'trigger':'run',       'source':'start',      'dest': 'processing'},
    {'trigger':'cancel',    'source':'processing', 'dest': 'warn'},
    {'trigger':'success',   'source':'processing', 'dest': 'exit'},
    {'trigger':'trouble',   'source':'processing', 'dest': 'error'},]

class Model(object):
    def action_finalize(self, event):
        if event.state.is_Compleat:
            print('Compleat!')

model = Model()
machine = CustomMachine(model=model, transitions=transitions, states=states, initial=states[0], 
                        auto_transitions=False, ordered_transitions=False, send_event=True,
                        finalize_event='action_finalize')

# machine = GraphMachine(model=model, transitions=transitions, states=states, initial=states[0], 
#                        auto_transitions=False, ordered_transitions=False, send_event=True,
#                        finalize_event='action_finalize')
                        


# filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test/_s5.png'
# model.get_graph().draw(filename, prog='dot', format='png')

# model.get_graph().draw('my_state_diagram.png', prog='dot')



print(model.run())

print(model.state)
# 'processing'
# print(model.trouble())      # error状態へ遷移するトリガーイベント
# Traceback (most recent call last):
# ～略～
# transitions.core.MachineError: "Error state 'error' reached!"
# print(model.state)
# 'error'