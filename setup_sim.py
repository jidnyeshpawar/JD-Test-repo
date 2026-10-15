import pybullet as p
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())
p.setGravity(0, 0, -9.8)

plane = p.loadURDF('plane.urdf')
box = p.loadURDF('cube.urdf', [0, 0, 3])

for _ in range(240):
    p.stepSimulation()
    time.sleep(1/240)

p.disconnect()
