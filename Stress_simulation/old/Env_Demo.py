import random
from environment_only import Environment


class Agent(): # エージェントを定義

    def __init__(self, env):
        self.actions = env.actions

    def policy(self, state):
        return random.choice(self.actions)


def main(): # 環境内でエージェントを動作させるコードを実装
    N = int(input("試行回数 N = "))
    # Make grid environment.
    grid = [
        [1],
        [0],
        [0],
        [0],
        [-1]
    ]
    # grid = [
    # [0, 0, 0, 1],
    # [0, 9, 0, -1],
    # [0, 0, 0, 0]
    # ]
    env = Environment(grid)
    agent = Agent(env)

    # Try 10 game.
    for i in range(N):
        # Initialize position of agent.
        state = env.reset()
        total_reward = 0
        done = False

        while not done:
            action = agent.policy(state)
            next_state, reward, done = env.step(action)
            total_reward += reward
            state = next_state

        print("\nEpisode {}: Agent gets {} reward.\n".format(i, total_reward))


if __name__ == "__main__":
    main()