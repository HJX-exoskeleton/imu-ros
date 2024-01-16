import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
file_path = '/home/hjx/handsfree/imu_data_record/hfi_a9_timer/imu_data_a9_timer.csv'  # Replace with your file path
imu_data = pd.read_csv(file_path)

# New upper and lower limits for the group size
upper_limit = 80
lower_limit = 40
final_group_constraint = 0.90  # 90% of the optimal group size

# Calculate the total number of rows in the dataset
total_rows = len(imu_data)

# Calculating the optimal group size within the specified range
group_sizes = np.arange(lower_limit, upper_limit + 1)
optimal_group_size = min(group_sizes, key=lambda x: abs(total_rows % x - x * final_group_constraint))

# Group the data using the new optimal group size
imu_data_grouped_adaptive = imu_data.groupby(np.arange(len(imu_data)) // optimal_group_size).mean()

# Check the size of the last group with the new group size
last_group_size_adaptive = len(imu_data) % optimal_group_size

# Drop the last group if it doesn't meet the 90% threshold of the new group size
if last_group_size_adaptive < optimal_group_size * final_group_constraint:
    discarded_group_size = last_group_size_adaptive
    imu_data_grouped_adaptive = imu_data_grouped_adaptive[:-1]
else:
    discarded_group_size = 0

# 绘制图表
global_line_width = 2  # 绘制曲线的粗细

# 加速度图
fig_acc, ax_acc = plt.subplots(figsize=(10, 6))
ax_acc.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['X_Acceleration'], label='X_Acceleration', linewidth = global_line_width)
ax_acc.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Y_Acceleration'], label='Y_Acceleration', linewidth = global_line_width)
ax_acc.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Z_Acceleration'], label='Z_Acceleration', linewidth = global_line_width)
ax_acc.set_title('Acceleration data changes over time')
ax_acc.set_xlabel('Adaptive grouping (indexing)')
ax_acc.set_ylabel('Acceleration(m/s²)')
ax_acc.legend()

# 角速度图
fig_ang_vel, ax_ang_vel = plt.subplots(figsize=(10, 6))
ax_ang_vel.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['X_AngularVelocity'], label='X_AngularVelocity', linewidth = global_line_width)
ax_ang_vel.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Y_AngularVelocity'], label='Y_AngularVelocity', linewidth = global_line_width)
ax_ang_vel.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Z_AngularVelocity'], label='Z_AngularVelocity', linewidth = global_line_width)
ax_ang_vel.set_title('AngularVelocity data changes over time')
ax_ang_vel.set_xlabel('Adaptive grouping (indexing)')
ax_ang_vel.set_ylabel('AngularVelocity(rad/s)')
ax_ang_vel.legend()

# 欧拉角图
fig_euler, ax_euler = plt.subplots(figsize=(10, 6))
ax_euler.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Euler_X'], label='Euler_X', linewidth = global_line_width)
ax_euler.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Euler_Y'], label='Euler_Y', linewidth = global_line_width)
ax_euler.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Euler_Z'], label='Euler_Z', linewidth = global_line_width)
ax_euler.set_title('Euler angle data changes over time')
ax_euler.set_xlabel('Adaptive grouping (indexing)')
ax_euler.set_ylabel('Euler angle(°)')
ax_euler.legend()

# 磁场图
fig_mag, ax_mag = plt.subplots(figsize=(10, 6))
ax_mag.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['X_Magnetometer'], label='X_Magnetometer', linewidth = global_line_width)
ax_mag.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Y_Magnetometer'], label='Y_Magnetometer', linewidth = global_line_width)
ax_mag.plot(imu_data_grouped_adaptive.index, imu_data_grouped_adaptive['Z_Magnetometer'], label='Z_Magnetometer', linewidth = global_line_width)
ax_mag.set_title('Magnetometer data changes over time')
ax_mag.set_xlabel('Adaptive grouping (indexing)')
ax_mag.set_ylabel('Magnetometer(μT)')
ax_mag.legend()

plt.show()

# 打印新的最佳组大小、丢弃的最后一个组的大小以及输入数据的维度
print("Optimal group size(最佳分组大小):", optimal_group_size)
print("Discarded group size(丢弃组大小):", discarded_group_size)
print("Input data dimension(输入数据的维度):", imu_data.shape)
print("Number of groups(分组的数量):", len(imu_data_grouped_adaptive))

# 保存分组后的数据到新的CSV文件
output_file_path = '/home/hjx/handsfree/imu_data_record/hfi_a9_timer/imu_data_a9_timer_slimmed.csv'  # 替换为您希望保存的路径
imu_data_grouped_adaptive.to_csv(output_file_path, index=False)


