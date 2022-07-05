import os
from matplotlib.pyplot import grid
import tornado.web
import tornado.escape
from Environment import Environment
from Planner import ValueIterationPlanner

import random



class Agent():

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)

def main():
        # data = tornado.escape.json_decode(self.request.body) 
        # grid = data["grid"]
        # plan_type = data["plan"]
        move_prob = 1.0 # 0.8  # default value



        # grid = []
        # grid = [
        # [0, 0, 0, 1],
        # [0, 9, 0, -1],
        # [0, 0, 0, 0]
        # ]
        grid = [
        [1],
        [0],
        [0],
        [0],
        # [0],
        # [0],
        # [0],
        # [0],
        # [0],
        [0]#[-1]
    ]

        env = Environment(grid, move_prob=move_prob)

        # agent = Environment.Agent(env)
        # agent = Agent(env)
        agent = Agent(env)

        

        planner = ValueIterationPlanner(env)

        result = planner.plan()
        planner.log.append(result)
        # self.write({"log": planner.log})
        print(f"log:\n {planner.log}")

        # Try 10 game.
        # for i in range(10):
        #     # Initialize position of agent.
        #     state = env.reset()
        #     total_reward = 0
        #     done = False

        #     while not done:
        #         action = agent.policy(state)
        #         next_state, reward, done = env.step(action)
        #         total_reward += reward
        #         state = next_state

        #     print("Episode {}: Agent gets {} reward.".format(i, total_reward))



if __name__ == "__main__":
    main()