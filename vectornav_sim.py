import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

class VectornavPublisher(Node):
    def __init__(self):
        super().__init__('vectornav_publisher_node')
        self.publisher_ = self.create_publisher(PoseWithCovarianceStamped, '/vectornav/pose', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        pose_with_covariance = PoseWithCovarianceStamped()
        pose_with_covariance.header = msg.header
        pose_with_covariance.pose = msg.pose

        #gazebo紫峰分のオフセットを追加
        pose_with_covariance.pose.pose.position.x += -3950640.6710130866
        pose_with_covariance.pose.pose.position.y += 3317155.34170999
        pose_with_covariance.pose.pose.position.z += 3738363.7332595424

        self.publisher_.publish(pose_with_covariance)

def main(args=None):
    rclpy.init(args=args)
    node = VectornavPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# UTM座標系
# 408335.218
# 3997006.045

# ECEDに変換
