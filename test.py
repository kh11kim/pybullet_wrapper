import gym
from pybullet_wrapper import *
import numpy as np
import pybullet as p
import time
env = PandaGymEnvColAvoid(render=True, reward_type="joint_col_obs")
#env = PandaDualArmGymEnv(render=True, level=0.1)
#env = gym.make("MyPandaDualArmReach-v0")
env.set_debug_mode()
obs = env.reset()

while True:
    #obs = env.reset()
    #env.render("human")
    action = env.action_space.sample()
    obs_, reward, done, info = env.step(action)
    env.do_debug_mode()
    print(reward)
    time.sleep(0.1)

input()