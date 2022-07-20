import glob
from PIL import Image
 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#フォルダ名を入れます
# folderName = "/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation"
folderName = "/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/fig"
     
#該当フォルダから画像のリストを取得。読み込みたいファイル形式を指定。ここではpng
picList = glob.glob(folderName + "\*.png")
     
#figオブジェクトの作成
fig = plt.figure()
     
#空のリスト作成
ims = []
print("piclist:{}".format(picList))
     
#画像ファイルを空のリストの中に1枚ずつ読み込み
for i in range(len(picList)):
         
    #読み込んで付け加えていく
    tmp = Image.open(picList[i])
    ims.append([plt.imshow(tmp)])     
     
#アニメーション作成
ani = animation.ArtistAnimation(fig, ims, interval=300, repeat_delay=1000)

#アニメーション保存。ファイル名を入れてください。ここではtest.gif
# ani.save("test.gif")
# s = ani.to_jshtml()
# with open( 'anim.gif', 'w') as f:
#     f.write(s)
# ani.save('ani.gif', writer='pillow')
# plt.show()
ims[0].save('/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/fig/pillow_imagedraw.gif',
               save_all=True, append_images=ims[1:], optimize=False, duration=40, loop=0)