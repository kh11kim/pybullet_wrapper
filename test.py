from pybullet_wrapper import Bullet, BulletCollisionChecker, BulletRobot, BulletSceneMaker, PandaDualArmEnv
import numpy as np
import pybullet as p

env = PandaDualArmEnv(render=True)
qtn = env.robot.panda1.get_ee_orientation()
mat = p.getMatrixFromQuaternion(qtn)

input()