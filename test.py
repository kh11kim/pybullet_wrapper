from pybullet_wrapper import Bullet, BulletCollisionChecker, BulletRobot, BulletSceneMaker, Panda
import numpy as np

bullet = Bullet(render=True)
scene_maker = BulletSceneMaker(bullet)
robot = Panda(bullet)

scene_maker.create_plane(z_offset=-0.4)
scene_maker.create_table(length=0.7, width=0.7, height=0.4, x_offset=0)
bullet.place_visualizer(
    target_position=np.zeros(3), 
    distance=1.6, 
    yaw=45, 
    pitch=-30
)

checker = BulletCollisionChecker(bullet)
for i in range(100):
    robot.get_random_joint_angles(set=True)
    if checker.is_collision():
        a = 1


input()