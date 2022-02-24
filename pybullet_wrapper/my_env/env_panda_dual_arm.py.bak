import gym
import numpy as np
from ..core import Bullet
from ..scene_maker import BulletSceneMaker
from ..my_robot import PandaDualArm

class PandaDualArmEnv:
    def __init__(self, render=False):
        self.is_render = render
        self.bullet = Bullet(render=render)
        self.scene_maker = BulletSceneMaker(self.bullet)
        self.robot = PandaDualArm(self.bullet)
        self._make_env()

    def _make_env(self):
        self.scene_maker.create_plane(z_offset=-0.4)
        self.scene_maker.create_table(length=1.0, width=1.0, height=0.4, x_offset=0)
        self.bullet.place_visualizer(
            target_position=np.zeros(3), 
            distance=1.6, 
            yaw=45, 
            pitch=-30
        )
    
    def render(
        self,
        mode: str,
        width: int = 720,
        height: int = 480,
        target_position: np.ndarray = np.zeros(3),
        distance: float = 1.4,
        yaw: float = 45,
        pitch: float = -30,
        roll: float = 0,
    ):
        return self.bullet.render(
            mode,
            width=width,
            height=height,
            target_position=target_position,
            distance=distance,
            yaw=yaw,
            pitch=pitch,
            roll=roll,
        )