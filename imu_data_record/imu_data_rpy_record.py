import rospy
import tf
from tf.transformations import *
from sensor_msgs.msg import Imu
import time

# 定义记录开始和结束时间
start_time = time.time()  # 记录开始时间
record_duration = 6  # 设置记录持续时间，这里设置为6秒，您可以根据需要进行调整
end_time = start_time + record_duration  # 记录结束时间

# 打开文件以写入数据
# file_path = '/home/hjx/handsfree/imu_data_record/rpy_timer/imu_data_rpy_timer.txt'  # txt文件路径
file_path = '/home/hjx/handsfree/imu_data_record/rpy_timer/imu_data_rpy_timer.csv'  # csv文件路径
file = open(file_path, 'w')

def callback(data):
    if time.time() < end_time:  # 在规定的时间段内执行记录
        (r, p, y) = tf.transformations.euler_from_quaternion(
            (data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w))
        # 由于是弧度制，下面将其改成角度制看起来更方便
        imu_data = "Roll = %f, Pitch = %f, Yaw = %f" % (r * 180 / 3.1415926, p * 180 / 3.1415926, y * 180 / 3.1415926)
        rospy.loginfo(imu_data)

        # 将数据写入文件
        file.write(imu_data + '\n')
    else:
        file.close()  # 规定时间结束后关闭文件
        rospy.signal_shutdown("Recording completed.")  # 停止ROS节点


def get_imu():
    rospy.init_node('get_imu', anonymous=True)
    rospy.Subscriber("/handsfree/imu", Imu, callback)  # 接受topic名称
    rospy.spin()


if __name__ == '__main__':
    get_imu()
