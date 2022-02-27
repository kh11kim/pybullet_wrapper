import gym
from pybullet_wrapper import *
import numpy as np
import pybullet as p

env = PandaDualArmGymEnvSingle(render=True, level=0.5)
#env = PandaDualArmGymEnv(render=True, level=0.1)
#env = gym.make("MyPandaDualArmReach-v0")
obs = env.reset()
for i in range(100):
    #obs = env.reset()
    env.render("human")
    action = env.action_space.sample()
    obs_, reward, done, info = env.step(action)

input()