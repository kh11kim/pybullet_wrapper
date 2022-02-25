from pybullet_wrapper import PandaDualArmGymEnv
import numpy as np
import pybullet as p

env = PandaDualArmGymEnv(render=True)
obs = env.reset()
for i in range(100):
    obs = env.reset()
    env.render("human")
    #action = env.action_space.sample()
    #obs_, reward, done, info = env.step(action)

input()