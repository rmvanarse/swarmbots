#Hostnumber $1
#Cmd: $bash/multimaster.bash <hostnumber>
base=11310
a=`expr $base + $1`
echo $a
export ROS_MASTER_URI=http://localhost:$a
roscore --port $a >/dev/null 2>&1 &
echo $ROS_MASTER_URI

#trial commit
