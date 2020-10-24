# rosbag_analyzer

## To analyze your bag files, follow the steps below:

1) Clone the repository using:
git clone https://github.com/alvarobelmontebaeza/rosbag_analyzer

2) Go to the repo, and put all bagfiles that you want to analyze in the bagfiles/ directory.

3) Compile the ROS package with "dts devel build -f"

4) Run the container with the following command:
docker run -it -v <path_to_rosbag_analyzer/bagfiles>:/bagfiles duckietown/rosbag_analyzer:v2-amd64

where <path_to_rosbag_analyzer/bagfiles> is the path in your machine to the rosbag_analyzer/bagfiles directory.

5) Enjoy your bagfiles Time analysis!