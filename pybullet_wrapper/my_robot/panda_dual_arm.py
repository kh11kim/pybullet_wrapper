import numpy as np
from pybullet_wrapper.core import Bullet
from pybullet_wrapper.my_robot import Panda

class PandaDualArm:
    def __init__(
        self, 
        bullet:Bullet, 
        panda1_position=[0,0.2,0],
        panda2_position=[0,-0.2,0],
    ):
        #name = "panda_dualarm"
        self.bullet = bullet
        self.panda1 = Panda(self.bullet, name="panda1", base_pos=panda1_position)
        self.panda2 = Panda(self.bullet, name="panda2", base_pos=panda2_position)
        self.joint_ll = np.hstack([self.panda1.joint_ll, self.panda2.joint_ll])
        self.joint_ul = np.hstack([self.panda1.joint_ul, self.panda2.joint_ul])
        self.n_joints = 14
    
    def set_joint_angles(self, joints):
        assert len(joints) == self.n_joints
        self.panda1.set_joint_angles(joints[:7])
        self.panda2.set_joint_angles(joints[7:])

    def get_joints(self):
        return np.hstack([self.panda1.get_joint_angles(), self.panda2.get_joint_angles()])
    
    def get_random_joints(self, set=False):
        return np.hstack([self.panda1.get_random_joint_angles(set), self.panda2.get_random_joint_angles(set)])
    
    def get_link_pos(self, link):
        return np.hstack([self.panda1.get_link_position(), self.panda2.get_link_position()])

    def get_ee_pos(self):
        return np.hstack([self.panda1.get_ee_position(), self.panda2.get_ee_position()])