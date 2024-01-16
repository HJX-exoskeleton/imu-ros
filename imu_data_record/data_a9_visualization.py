import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter1d

# 加载CSV文件
file_path = '/home/hjx/handsfree/imu_data_record/hfi_a9_timer/imu_data_a9_timer.csv'
data = pd.read_csv(file_path)

# 将时间戳转换为更可读的格式
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='s')

# 定义科学论文颜色方案（ColorBrewer Set2）
colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']

line_width = 3.6  # 曲线的粗细大小设置

# 创建一个函数来绘制数据（分图）
def plot_data(data, columns, title, y_label, line_width):
    plt.figure(figsize=(15, 5))
    for i, col in enumerate(columns):
        x = data['Timestamp']
        y = data[col]
        color = colors[i % len(colors)]  # 使用不同颜色
        # 添加柔化边缘效果
        smoothed_y = gaussian_filter1d(y, sigma=500)
        plt.plot(x, smoothed_y, label=col, linewidth=line_width, color=color)

    plt.title(title)
    plt.xlabel('Timestamp')
    plt.ylabel(y_label)
    plt.legend()
    plt.grid(True)
# 绘制加速度数据（添加柔化边缘效果，使用不同颜色）
plot_data(data, ['X_Acceleration', 'Y_Acceleration', 'Z_Acceleration'], 'Acceleration data changes over time',
          'Acceleration(m/s²)', line_width)
# 绘制角速度数据（添加柔化边缘效果，使用不同颜色）
plot_data(data, ['X_AngularVelocity', 'Y_AngularVelocity', 'Z_AngularVelocity'],
          'Angular velocity data changes over time', 'AngularVelocity(rad/s)', line_width)
# 绘制欧拉角数据（添加柔化边缘效果，使用不同颜色）
plot_data(data, ['Euler_X', 'Euler_Y', 'Euler_Z'], 'Euler angle changes over time', 'Euler angle(°)', line_width)
# 绘制磁力计数据（添加柔化边缘效果，使用不同颜色）
plot_data(data, ['X_Magnetometer', 'Y_Magnetometer', 'Z_Magnetometer'], 'Magnetometer data changes over time',
          'Magnetometer(μT)', line_width)


# 创建一个函数来绘制数据(全部)
def plot_data_all(data, columns, title, y_label, line_width, ax=None):
    if ax is None:
        ax = plt.gca()
    for i, col in enumerate(columns):
        x = data['Timestamp']
        y = data[col]
        color = colors[i % len(colors)]  # 使用不同颜色
        # 添加柔化边缘效果
        smoothed_y = gaussian_filter1d(y, sigma=500)
        ax.plot(x, smoothed_y, label=col, linewidth=line_width, color=color)

    ax.set_title(title)
    ax.set_xlabel('Timestamp')
    ax.set_ylabel(y_label)
    ax.legend()
    ax.grid(True)
# 创建一个包含四个子图的图表
fig, axes = plt.subplots(4, 1, figsize=(15, 20), sharex=True)
# 绘制加速度数据（添加柔化边缘效果，使用不同颜色）
plot_data_all(data, ['X_Acceleration', 'Y_Acceleration', 'Z_Acceleration'], 'Acceleration data changes over time',
          'Acceleration(m/s²)', line_width, ax=axes[0])
# 绘制角速度数据（添加柔化边缘效果，使用不同颜色）
plot_data_all(data, ['X_AngularVelocity', 'Y_AngularVelocity', 'Z_AngularVelocity'],
          'Angular velocity data changes over time', 'AngularVelocity(rad/s)', line_width, ax=axes[1])
# 绘制欧拉角数据（添加柔化边缘效果，使用不同颜色）
plot_data_all(data, ['Euler_X', 'Euler_Y', 'Euler_Z'], 'Euler angle changes over time', 'Euler angle(°)', line_width, ax=axes[2])
# 绘制磁力计数据（添加柔化边缘效果，使用不同颜色）
plot_data_all(data, ['X_Magnetometer', 'Y_Magnetometer', 'Z_Magnetometer'], 'Magnetometer data changes over time',
          'Magnetometer(μT)', line_width, ax=axes[3])
# 调整子图之间的间距
plt.tight_layout()

# 显示图表
plt.show()