import rosbag
from rosbag.bag import Bag
import os
import numpy as np

if __name__ == '__main__':

    # Read bag files in /bagfiles folder, which is a mounted volume of
    # rosbag_analizer/bagfiles
    bags = []
    for file in os.listdir("/bagfiles"):
        bags.append(Bag(os.path.join("/bagfiles",file)))

    # Analyze each of the found rosbags
    for bag in bags:
        # info_dict = yaml.load(bag._get_yaml_info())
        print(bag)
        msg_count = 0
        time_diff = np.array([])
        t_prev= 0.0
        

        # Analyze camera image topic
        for topic, msg, t in bag.read_messages(topics=['/sora/camera_node/image/compressed']):
            msg_count+=1
            curr_time = t.to_sec()
            time_diff = np.append(time_diff,curr_time-t_prev)
            t_prev=curr_time            

            
        print("/sora/camera_node/image/compressed:")
        print("  num_messages: %s" % msg_count)
        print("  period:")
        print("    min: %s" % np.amin(time_diff[1:]))
        print("    max: %s" % np.amax(time_diff[1:]))
        print("    average: %s" % np.average(time_diff[1:]))
        print("    median: %s" % np.median(time_diff[1:]))
        print("\t")

        # info_dict = yaml.load(bag._get_yaml_info())
        msg_count = 0
        time_diff = np.array([])
        t_prev= 0.0

        # Analyze wheel comand topic
        for topic, msg, t in bag.read_messages(topics=['/sora/wheels_driver_node/wheels_cmd']):
            msg_count+=1
            curr_time = t.to_sec()
            time_diff = np.append(time_diff,curr_time-t_prev)
            t_prev=curr_time            

            
        print("/sora/wheels_driver_node/wheels_cmd:")
        print("  num_messages: %s" % msg_count)
        print("  period:")
        print("    min: %s" % np.amin(time_diff[1:]))
        print("    max: %s" % np.amax(time_diff[1:]))
        print("    average: %s" % np.average(time_diff[1:]))
        print("    median: %s" % np.median(time_diff[1:]))
        print("\t")            