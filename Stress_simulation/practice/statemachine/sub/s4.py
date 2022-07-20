from transitions import Machine
from transitions.extensions.states import add_state_features, Tags

@add_state_features(Tags)
class CustomMachine(Machine):
    pass

tag_name = 'hoge'
states = ['A', 'B', {'name': 'C', 'tags':tag_name }, {'name': 'D', 'tags':tag_name }]  

class Model(object):
    def action_finalize(self, event):
        print('state {}'.format(self.state))            # self.stateはstr型
        if getattr(event.state, 'is_' + tag_name):      # event.stateはTags(State継承クラス)型, タグの付いた状態のみ処理を実施
            print('特別なhogehoge')

model = Model()
machine = CustomMachine(model=model, states=states, initial=states[0], 
                        auto_transitions=False, ordered_transitions=True, 
                        send_event=True, finalize_event='action_finalize')


# filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/test/_s4.png'
# model.get_graph().draw(filename, prog='dot', format='png')


print(model.state)             # 現在の状態を確認
# 'A'
print( model.next_state())      # 次の状態に遷移
# state B
# True
print( model.next_state())      # 次の状態に遷移
# state C
# 特別なhogehoge
# True
print( model.next_state() )     # 次の状態に遷移
# state D
# 特別なhogehoge
# True
print( model.next_state())      # 次の状態に遷移
# state A
# True