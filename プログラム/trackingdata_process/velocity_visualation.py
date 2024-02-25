# %% 
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
#%%
import json
json_open = open('json.json', 'r')
trajectory = json.load(json_open)
#%%
#### calculate velocities of ants
fps = 30
def cal_velocity(trajectory):
    velocity_dic = {}
    for i in range(1, len(trajectory)+1):
            if i not in velocity_dic:
                velocity_dic[str(i)] = []
            frame, x, y = zip(*trajectory[str(i)])
            velocities_x = np.diff(x) 
            velocities_y = np.diff(y) 
            total_integrated_velocity = np.sqrt(velocities_x**2 + velocities_y**2)
            velocity_dic[str(i)].append(total_integrated_velocity)
    return velocity_dic
#%%
velocity_dic = cal_velocity(trajectory)
#%%
###count number of ant exists on each frame
def count_ant(velocity_dic):
    id_count = []
    for i in range(265):
        count = 0 
        for j in range(1, len(velocity_dic)+1):
            if np.isnan(velocity_dic[str(j)][0][i]):
                    pass
            else:
                    count += 1
        id_count.append(count)
    return id_count
#%%
id_count = count_ant(velocity_dic)    
print(id_count)
#%%
### check length of array without nan value
def non_nan_length(arr):
     return np.sum(np.logical_not(np.isnan(arr)))

#%%
### calculate average velocity of each frame
def avg_velo_eachFrame(velocity_dic,id_count):
    avg_eachFrame = np.nansum([velocity_dic[str(i)][0] for i in range(1,20)], axis=0)
    avg_eachFrame = avg_eachFrame/id_count
    return avg_eachFrame
#%%
result_array = avg_velo_eachFrame(velocity_dic, id_count)
#%%
def velocity(velocity_dic,id_count, result_array):
    ###draw velocity all frames
    id_count = count_ant(velocity_dic)
    for key, value in velocity_dic.items():
        plt.plot(value[0] ,label = f"{key}")
    plt.xlabel('frame')
    plt.ylabel('pixel/frame')
    plt.title('velocity all frame')
    plt.legend(loc = "best")
    plt.show()
    ### draw sum velocity of all ants in all frames:
    plt.plot(result_array)
    plt.xlabel('frame')
    plt.ylabel('pixel/frame')
    plt.title('average velocity in all frames ')
    plt.show()
    ### draw average velocity of each ant
    for key, value in velocity_dic.items():
        average = np.nansum(value[0])/non_nan_length(value[0])
        average
        plt.bar(key, average, label = f"{key}")
    plt.xlabel('''ant's id''')
    plt.ylabel('pixel/frame')
    plt.xticks([i for i in range(1,20)])
    plt.title("average velocity of ants")
    #plt.legend()
    plt.show()
#%%
velocity(velocity_dic,id_count, result_array)
# %%
### high speed and low speed of ants
def cls_all_frames(velocity_dic, id_count):
        low_id_number = []
        high_id_number = []
        ### calculate average velocity of all ants in each frame
        result_array = np.nansum([velocity_dic[str(i)][0] for i in range(1,len(velocity_dic)+1)], axis=0)
        result_array = result_array/id_count
        for i in range(len(result_array)):
            high_count = 0
            low_count = 0
            for j in range(1, len(velocity_dic)+1):
                  if np.isnan(velocity_dic[str(j)][0][i]):
                        pass
                  else:
                    if velocity_dic[str(j)][0][i] < result_array[i]:
                         low_count += 1
                       
                    else:
                         high_count += 1
            low_id_number.append(low_count)
            high_id_number.append(high_count)
        ###number of ants divided by velocity
        plt.bar( [i for i in range(0,265)],low_id_number, label='low_speed_id')
        plt.bar([i for i in range(0,265)],high_id_number,  bottom=low_id_number, label= "high_speed_id")
        plt.yticks(range(1,20))
        plt.xlabel("frame")
        plt.ylabel("number of ants")
        plt.legend()     
        plt.show()
        ### % of ants divided by velocity


        combined1 = [x / (x+y) * 100 for (x, y) in zip(low_id_number,high_id_number)]
        combined2 = [y / (x+y) * 100 for (x, y) in zip(low_id_number,high_id_number)]
        combined3 = [(x+y)  for (x, y) in zip(low_id_number,high_id_number)]

        plt.bar( [i for i in range(len(combined1))],combined1, label='low_speed_id')
        plt.bar([i for i in range(len(combined2))],combined2,  bottom=combined1, label= "high_speed_id")
        plt.xlabel("frame")
        plt.ylabel("percent of ant")
        plt.legend()     
        plt.show()
        
        plt.bar( [i for i in range(0,265)],combined3)
        plt.xlabel("frame")
        plt.ylabel("number of ant")
        plt.yticks(range(1,20))

        plt.legend()     
        plt.show()

        
        


# %%
cls_all_frames(velocity_dic, id_count)
# %%
# draw trajectory of each ant
from draw_trajectory import draw_trajectory_byId
draw_trajectory_byId(trajectory, 16)

# %%
for i in [6,1,3,13,9,5]:
        plt.plot( velocity_dic[str(i)][0], label = i)
        plt.xlabel('frame')
        plt.ylabel('pixel/frame')
        plt.title('velocity all frame')
        plt.legend(loc = "best")
        plt.show()
# %%
### calculate average speed of ants
average_dict = {}
for key, value in velocity_dic.items():
        average = np.nansum(value[0])/non_nan_length(value[0])
        if key not in average_dict:
             average_dict[key] = []
        average_dict[key].append(average)
#%%
average_dict = dict(sorted(average_dict.items(), key=lambda item: item[1]))
# %%
import statistics
# draw trajectory of low speed ants
def draw_trajectory(trajectory):
    #visulation all frames
    for i in [6,1,3,13,9,5]:
        frame, x_values, y_values = zip(*trajectory[str(i)])
        plt.scatter( np.nanmean(x_values),np.nanmean(y_values),label = f"{i}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, 800)
    plt.ylim(0, 600)
    plt.legend()
    plt.show() 
draw_trajectory(trajectory)
# %%
def draw_trajectory(trajectory):
    #visulation all frames
    for i in range(1,len(trajectory)+1):
        frame, x_values, y_values = zip(*trajectory[str(i)])
        plt.plot(x_values,y_values, label = f"{i}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0, 800)
    plt.ylim(0, 600)
    plt.legend()
    plt.show() 

# %%
def find_first_not_nan(lst):
    first_not_nan = None
    last_not_nan = None

    for value in lst:
        if not math.isnan(value):
            if first_not_nan is None:
                first_not_nan = value
            last_not_nan = value

    return first_not_nan
def find_last_not_nan(lst):
    first_not_nan = None
    last_not_nan = None

    for value in lst:
        if not math.isnan(value):
            if first_not_nan is None:
                first_not_nan = value
            last_not_nan = value

    return last_not_nan
### draw 方向
def draw_hoko(trajectory,id):
        frame, x_values, y_values = zip(*trajectory[str(i)])
        point = {
        'start': [find_first_not_nan(x_values),find_first_not_nan(y_values)],
        'end': [find_last_not_nan(x_values), find_last_not_nan(y_values)]
    }
        plt.plot(*point['start'], 'o', color="red",label = i)
        plt.plot(*point['end'], 'o', color="blue")

        plt.annotate('', xy=point['end'], xytext=point['start'],
                arrowprops=dict(shrink=0, width=1, headwidth=8, 
                                headlength=10, connectionstyle='arc3',
                                facecolor='gray', edgecolor='gray')
               )

        plt.xlim([0, 800])
        plt.ylim([0, 600])
        plt.legend()
        plt.show()

for i in [4,7]:
     draw_hoko(trajectory,i)
# %%
def draw_trajectory_byId(trajectory, id):
    frame, x_values, y_values = zip(*trajectory[str(id)])
    plt.plot(x_values, y_values, label = f"{id}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim([0, 800])
    plt.ylim([0, 600])
    plt.legend()
    plt.title(f"trajectory")

# %%
for i in [4,10,16,17,18]:
        plt.plot( velocity_dic[str(i)][0], label = i)
        plt.xlabel('frame')
        plt.ylabel('pixel/frame')
        plt.title('velocity all frame')
        plt.legend(loc = "best")
        plt.show()
# %%
for i in [4,16,10,17]:
     draw_trajectory_byId(trajectory,i)
# %%
draw_trajectory_byId(trajectory,18)

# %%
