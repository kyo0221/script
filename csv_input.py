import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import csv

class Converter(Node):
    def __init__(self):
        super().__init__("gps_csv_node")
        self.subscription = self.create_subscription(NavSatFix, "/vectornav/gnss", self.callback, 10)
        self.subscription
        self.get_logger().info("vctornav/gnssをcsvファイルにします。")

        self.csv_file = open('gps_data_r.csv', mode='w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(['Latitude', 'Longitude'])

    def callback(self, msg):
        latitude = msg.latitude
        longitude = msg.longitude
        print(latitude, longitude)
        self.csv_writer.writerow([latitude, longitude])
        # self.get_logger().info(f'Latitude: {latitude}, Longitude: {longitude}')

    def destroy_node(self):
        self.csv_file.close()
        super().destroy_node()



def main():
    rclpy.init()
    node = Converter()

    rclpy.spin(node)
    node.destroy_node()

    rclpy.shutdown()

if __name__ == "__main__":
    main()