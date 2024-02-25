# %%

import os
# import sys
import numpy as np
import pandas as pd

# %%

# frame class_id individual_id x y w h -1 -1 -1 -1
# Load data

in_file = 'input.txt'
df = pd.read_csv(in_file, sep=' ', header=None)
# %%
df.columns = ['frame', 'class_id', 'individual_id', 'x', 'y', 'w', 'h', 'a', 'b', 'c', 'd', 'dummy']
# %%
df
# %%
df['individual_id'].unique()

# 縦軸: frame 横軸: individual_id で存在するかどうかを確認する表を作成
df_pivot = df.pivot_table(index='frame', columns='individual_id', values='x', aggfunc='count')
df_pivot

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# df_pivot を可視化
plt.figure(figsize=(20, 10))
sns.heatmap(df_pivot, cmap='Blues')
plt.xlabel("invidual_id(i)", fontsize=16)
plt.ylabel("frame(t)", fontsize=16)

plt.savefig('existence.png')
# colorbarいらないが・・
plt.show()
# %%
# 各個体が存在するフレーム数を確認
num_appeared_frames_i = df_pivot.sum(axis=0).sort_values(ascending=False)
num_unique_ids = len(num_appeared_frames_i)

# %%
# プロット
threshold = 75
plt.figure(figsize=(20, 10))
plt.bar(range(num_unique_ids), num_appeared_frames_i.values)
# 全ての横軸のラベルを表示
plt.xticks(range(num_unique_ids), num_appeared_frames_i.index)
plt.axhline(y=threshold, color='red', linestyle='--')
plt.xlabel('individual_id(i)',fontsize=16)
plt.ylabel('num_appeared_frames(t)',fontsize=16)
plt.savefig('num_appeared_frames.png')
plt.show()


# %%
### get the id that not good for data
condition_clear_id = num_appeared_frames_i.values <= 75
clear_id = num_appeared_frames_i.index[condition_clear_id]

# %%
condition = df["individual_id"].isin(list(clear_id))
df.drop(df[condition].index, inplace=True)
df = df.reset_index(drop=True)

#%%
new_unique_values = np.arange(1, 20)
df["individual_id"].replace(to_replace=df["individual_id"].unique(), value=new_unique_values, inplace=True)
df["x_center"] = (df["x"] + df["h"])/2
df["y_center"] = (df["y"] + df["w"])/2

#%%

df_pivot = df.pivot_table(index='frame', columns='individual_id', values='x', aggfunc='count')
import matplotlib.pyplot as plt
import seaborn as sns
num_appeared_frames_i = df_pivot.sum(axis=0).sort_values(ascending=False)
num_unique_ids = len(num_appeared_frames_i)
# df_pivot を可視化 after process data
plt.figure(figsize=(20, 10))
sns.heatmap(df_pivot, cmap='Blues')
plt.savefig('existence_after.png')
# colorbarいらないが・・
plt.show()
plt.bar(range(num_unique_ids), num_appeared_frames_i.values)
# 全ての横軸のラベルを表示
plt.xticks(range(num_unique_ids), num_appeared_frames_i.index)
plt.xlabel('individual_id(t)')
plt.ylabel('num_appeared_frames(t)')
plt.savefig('num_appeared_frames.png')
plt.show()

#%% 
df.to_csv('tracking_after.txt', index=False)

# %%
