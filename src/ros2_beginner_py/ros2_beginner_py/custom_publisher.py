import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from tutorial_interfaces.msg import Num


class CustomPublisher(Node):

    def __init__(self):
        super().__init__('custom_publisher')
        self.publisher = self.create_publisher(Num, 'topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Num()
        msg.num = self.count
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.num}"')
        self.count += 1


def main(args=None):
    try:
        with rclpy.init(args=args):
            rclpy.spin(CustomPublisher())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
