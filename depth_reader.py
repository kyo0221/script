import rclpy
from rclpy.node import Node
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class DepthPixelReader(Node):
    def __init__(self):
        super().__init__('depth_pixel_reader')
        self.subscription = self.create_subscription(
            Image,
            '/depth_camera/depth/image_raw',
            self.image_callback,
            10)
        self.bridge = CvBridge()
        self.x = None
        self.y = None
        
    def image_callback(self, msg):
        if self.x is None or self.y is None:
            try:
                self.x = int(input("X座標を入力してください: "))
                self.y = int(input("Y座標を入力してください: "))
            except ValueError:
                self.get_logger().error("無効な入力です。整数を入力してください。")
                return

        try:
            # ROSのImageメッセージをOpenCVの画像に変換
            depth_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            
            # 指定されたピクセルの深度値を取得
            if 0 <= self.x < depth_image.shape[1] and 0 <= self.y < depth_image.shape[0]:
                depth_value = depth_image[self.y, self.x]
                self.get_logger().info(f'Depth at ({self.x}, {self.y}): {depth_value} meters')
                
                # 画像にポイントをプロット
                depth_viz = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
                depth_viz = cv2.applyColorMap(depth_viz, cv2.COLORMAP_JET)
                cv2.circle(depth_viz, (self.x, self.y), 5, (0, 0, 255), -1)
                
                # 画像を表示
                cv2.imshow("Depth Image", depth_viz)
                cv2.waitKey(1)
            else:
                self.get_logger().warn('指定されたピクセル座標が画像の範囲外です')
        except Exception as e:
            self.get_logger().error(f'画像処理中にエラー発生: {e}')

def main():
    rclpy.init()
    node = DepthPixelReader()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

