import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_demo')
        self.declare_parameter('my_parameter', 'world')
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').value
        self.get_logger().info(f'Hello {my_param}!')


def main(args=None):
    try:
        with rclpy.init(args=args):
            rclpy.spin(ParameterNode())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
