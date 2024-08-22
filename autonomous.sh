#!/bin/bash

# /autonomousトピックにtrueをパブリッシュする
ros2 topic pub /autonomous std_msgs/msg/Bool "data: true"

