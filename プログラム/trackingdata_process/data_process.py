# %% 
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
#%%
file_name = "tracking_after.txt"
df = pd.read_csv(file_name, sep=',', header=0)
df
#%%
def get_trajectory_data(data_file):
    trajectory  = {}
    for i in range(len(data_file)):
        id = data_file["individual_id"][i]
        if id not in trajectory:
            trajectory[id] = []
        trajectory[id].append(tuple((int(data_file["frame"][i]),data_file["x_center"][i],data_file["y_center"][i])))
    for i in range(1,20):
        frame_1, x_values_1, y_values_1 = zip(*trajectory[int(i)])
        for j in range(min(data_file["frame"]), max(data_file["frame"])+1):
            if j not in frame_1:
                trajectory[int(i)].append((j, np.nan, np.nan))
        trajectory[int(i)] = sorted(trajectory[int(i)], key=lambda x:x[0], reverse=False)
    return trajectory
#%%
trajectory = get_trajectory_data(df)
### save dictionary file
import json
file_path = 'my_dict_1.json'
my_dict_serializable = {
    str(key): int(value) if isinstance(value, np.int64) else value
    for key, value in trajectory.items()}

# Save dictionary to a file
with open(file_path, 'w') as json_file:
    json.dump(my_dict_serializable, json_file)

# %%
import json
json_open = open('json.json', 'r')
trajectory = json.load(json_open)
#%%
trajectory["1"]
# %%
import numpy as np
fps = 30
def cal_velocity(trajectory, fps):
    velocity_dic = {}
    for i in range(1, len(trajectory)+1):
            if i not in velocity_dic:
                velocity_dic[str(i)] = []
            frame, x, y = zip(*trajectory[str(i)])
            velocities_x = np.diff(x) / fps
            velocities_y = np.diff(y) / fps
            total_integrated_velocity = np.sqrt(velocities_x**2 + velocities_y**2)
            velocity_dic[str(i)].append(total_integrated_velocity)
    return velocity_dic
#%%
velocity_dic = cal_velocity(trajectory,fps)# %%
import matplotlib.pyplot as plt
for key, value in velocity_dic.items():
        plt.plot(value[0] ,label = f"{key}")
        plt.xlabel('frame')
        plt.ylabel('pixel/frame')
        plt.title('velocity all frame')
        plt.legend(loc = "best")
        plt.show()
# %%
