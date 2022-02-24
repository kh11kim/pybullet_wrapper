from pybullet_wrapper import Bullet, BulletCollisionChecker, BulletRobot, BulletSceneMaker, PandaDualArmEnv
import numpy as np
import pybullet as p

env = PandaDualArmEnv(render=True)
pos = env.robot.panda1.get_ee_position()
orn = env.robot.panda1.get_ee_orientation()
joint_angles = env.robot.panda1.inverse_kinematics(pos, orn)
env.scene_maker.view_frame("ee1", pos, orn)
env.bullet.render()

input()