import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from tutorial_interfaces.msg import Num


class CustomSubscriber(Node):

    def __init__(self):
        super().__init__('custom_subscriber')
        self.subscription = self.create_subscription(
            Num, 'topic', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.num}"')


def main(args=None):
    try:
        with rclpy.init(args=args):
            rclpy.spin(CustomSubscriber())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
