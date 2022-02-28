import gym
from pybullet_wrapper import *
import numpy as np
import pybullet as p
import time

#env = PandaGymNewEnv(render=True, reward_type="")
#env = PandaDualArmGymEnv(render=True, level=0.1)
#env = gym.make("MyPandaDualArmReach-v0")
#env.set_debug_mode()
rewards = []
obs = env.reset()
for i in range(100):
    obs = env.reset()
    action = env.action_space.sample()
    obs_, reward, done, info = env.step(action)
    rewards.append(reward)
print(f"reward:{np.mean(rewards)}")
while True:
    #obs = env.reset()
    #env.render("human")
    action = env.action_space.sample()
    obs_, reward, done, info = env.step(action)
    env.do_debug_mode()
    print(reward)
    time.sleep(0.1)

input()