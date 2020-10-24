import rosbag
from rosbag.bag import Bag
import os
import numpy as np
from collections import defaultdict

if __name__ == '__main__':

    # Read bag files in /bagfiles folder, which is a mounted volume of
    # rosbag_analizer/bagfiles
    bags = []
    bag_names = []
    for file in os.listdir("/bagfiles"):
        bags.append(Bag(os.path.join("/bagfiles",file)))
        bag_names.append(file)

    idx = 0
    # Analyze each of the found rosbags
    for bag in bags:
        # Print current bagfile name
        print("===============================")
        print(bag_names[idx])
        print("===============================")
        idx +=1 

        # Extract information from bag file
        bag_info = defaultdict(list)
        for topic, msg, t in bag.read_messages():
            bag_info[topic].append((msg,t))

        for topic in bag_info.keys():
            # Initilialize variables for topic analysis
            msg_count = 0
            time_diff = np.array([])
            t_prev= 0.0        

            # Analyze information for each topic separately
            for msg, t in bag_info[topic]:
                msg_count+=1
                curr_time = t.to_sec()
                time_diff = np.append(time_diff,curr_time-t_prev)
                t_prev=curr_time            

            # Print time analysis of the current topic
            print(topic + ":")
            print("  num_messages: %s" % msg_count)
            print("  period:")
            print("    min: %.2f" % np.amin(time_diff[1:]))
            print("    max: %.2f" % np.amax(time_diff[1:]))
            print("    average: %.2f" % np.average(time_diff[1:]))
            print("    median: %.2f" % np.median(time_diff[1:]))
            print("\t")
            print("-------------------------------------")
        
        # Close bag file upon ending
        bag.close()
