# data_rpy_processor_regex
import re

# 定义一个函数，使用正则表达式来提取每行中的数字
def extract_numbers(line):
    # 正则表达式匹配所有的浮点数和负数
    return re.findall(r"[-+]?\d*\.\d+|\d+", line)

# 读取原始数据文件
with open('/home/hjx/handsfree/imu_data_record/rpy_timer/imu_data_rpy_timer.csv', 'r') as file:
    original_lines = file.readlines()

# 创建一个新的CSV文件用于保存处理后的数据
with open('/home/hjx/handsfree/imu_data_record/rpy_timer/imu_data_rpy_timer_processed_regex.csv', 'w') as output_file:
    for line in original_lines:
        numbers = extract_numbers(line)
        if len(numbers) >= 3:
            # 提取 Roll, Pitch, Yaw 的值
            roll, pitch, yaw = numbers[:3]
            # 写入提取的值到新的CSV文件
            output_file.write(f'{roll},{pitch},{yaw}\n')

print('数据处理完成，已保存为 imu_data_rpy_timer_processed_regex.csv 文件')

# 这段代码首先定义了一个函数 extract_numbers 来使用正则表达式从字符串中提取数字。
# 然后，它读取原始数据文件，对于文件中的每一行，使用这个函数来提取数字，
# 最后将提取的 Roll、Pitch 和 Yaw 值写入到一个新的CSV文件中。
