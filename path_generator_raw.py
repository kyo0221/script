#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Path


class PathGenerator(Node):
    def __init__(self) -> None:
        super().__init__("path_generator")
        self.publisher = self.create_publisher(Path, "/e2e_planner/path", 10)
        self.timer = self.create_timer(0.1, self.publish_path)  # 10 Hz
        self.path = self._build_path()

    def _build_path(self) -> Path:
        path = Path()
        path.header.frame_id = "map"
        for x in range(0, 11):
            pose = PoseStamped()
            pose.header.frame_id = "map"
            pose.pose.position.x = float(x)
            pose.pose.position.y = 0.0
            pose.pose.position.z = 0.0
            pose.pose.orientation.w = 1.0
            path.poses.append(pose)
        return path

    def publish_path(self) -> None:
        now = self.get_clock().now().to_msg()
        self.path.header.stamp = now
        for pose in self.path.poses:
            pose.header.stamp = now
        self.publisher.publish(self.path)


def main() -> None:
    rclpy.init()
    node = PathGenerator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
