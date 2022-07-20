import imageio
import os

# source_images_dir = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/'
source_images_dir = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/mdp_fig_class_for/'

image_list = []
for file_name in os.listdir(source_images_dir):
    _, ext = os.path.splitext(file_name)
    if ext == '.png':
        image_list.append(imageio.imread(source_images_dir + file_name))

# imageio.mimwrite('animation.gif', image_list, fps = 1)
imageio.mimwrite('anim_main_1.gif', image_list, fps = 0.8)
