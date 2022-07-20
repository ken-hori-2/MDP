from transitions import Machine
from transitions.extensions.states import add_state_features, Tags

# タグを使う場合はadd_state_featuresをつけて引数にTagsを指定し新たにCustomMachineクラスを定義
@add_state_features(Tags)
class CustomMachine(Machine):
    pass

# 状態の定義(タグ機能付き)
states = [{'name': 'A', 'tags': ['TagA', 'Init']},     # 状態AにTagAとInitというタグを付ける
          {'name': 'B', 'tags': 'TagB'},               # 状態BにTagBというタグを付ける
          {'name': 'C', 'tags': 'TagC'}]  

class Model(object):
    pass

model = Model()
machine = CustomMachine(model=model, states=states, initial=states[0]['name'], 
                        auto_transitions=False, ordered_transitions=True,)

# filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/s3.png'
# model.get_graph().draw(filename, prog='dot', format='png')

print(model.state)          # まずは現在の状態を確認
print(machine.get_state(model.state).tags)     #状態Aが持つタグの確認
# 'A'
# print(machine.get_state(model.state).is_Init)   # Initタグの確認
# True
print(" A:{}".format(machine.get_state(model.state).is_TagA))   # TagAタグの確認
# True
print(" B:{}".format(machine.get_state(model.state).is_TagB))   # TagBタグの確認
# False



# print(model.next_state())   # 次の状態に遷移
model.next_state()
print(model.state)          # 現在の状態を確認
print(machine.get_state(model.state).tags)     #状態Aが持つタグの確認

# print(machine.get_state(model.state).is_Init)   # Initタグの確認
# False
print(" A:{}".format(machine.get_state(model.state).is_TagA))   # TagAタグの確認
# False
print(" B:{}".format(machine.get_state(model.state).is_TagB))   # TagBタグの確認
# True

# print(model.next_state())   # 次の状態に遷移
model.next_state()
print(model.state)          # 現在の状態を確認
print(machine.get_state(model.state).tags)     #状態Aが持つタグの確認

# print(machine.get_state(model.state).is_Init)   # Initタグの確認
# False
print(" A:{}".format(machine.get_state(model.state).is_TagA))   # TagAタグの確認
# False
print(" B:{}".format(machine.get_state(model.state).is_TagB))   # TagBタグの確認
# False
print(" C:{}".format(machine.get_state(model.state).is_TagC))   # TagCタグの確認
# True





machine.get_state(model.state).tags.append('TagNew')    #タグの追加
print(machine.get_state(model.state).tags)