#%%
###import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %%

def draw_trajectory(trajectory, panic_frame):
    #visulation all frames
    for i in range(1,len(trajectory)+1):
        frame, x_values, y_values = zip(*trajectory[str(i)])
        plt.plot(x_values,y_values, label = f"{i}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show() 

    for i in range(1, len(trajectory)):
        frame, x_values, y_values = zip(*trajectory[i])
        x_values_1 = x_values[:panic_frame]
        y_values_1 = y_values[:panic_frame]
        plt.plot(x_values_1, y_values_1, label = f"{i}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show() 
    for i in range(1, len(trajectory)+1):
        
        frame, x_values, y_values = zip(*trajectory[f"{i}"])
        x_values_2 = x_values[panic_frame:]
        y_values_2 = y_values[panic_frame:]
        plt.plot(x_values_2, y_values_2, label = f"{i}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show() 
def draw_trajectory_byId(trajectory, id):
    frame, x_values, y_values = zip(*trajectory[str(id)])
    plt.plot(x_values, y_values, label = f"{id}")
    plt.scatter(x_values[0], y_values[0], color='red', label='Start')  
    plt.scatter(x_values[-1], y_values[-1], color='green', label='End')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title(f"trajectory")

