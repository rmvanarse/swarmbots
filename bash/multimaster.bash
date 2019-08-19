#Hostnumber $1
#Run: $bash/multimaster.bash <hostnumber>

export ROS_MASTER_URI=http://localhost:$a
roscore --port 11311 >/dev/null 2>&1 &
