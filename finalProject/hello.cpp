import mujoco
import os
mj_path = mujoco.utils.discover_mujoco()
xml_path = os.path.join(mj_path, 'model', 'humanoid.xml')
model = mujoco.load_model_from_path(xml_path)
sim = mujoco.MjSim(model)

print(sim.data.qpos)

sim.step()
print(sim.data.qpos)