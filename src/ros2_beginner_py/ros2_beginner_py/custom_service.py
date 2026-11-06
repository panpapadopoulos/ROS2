import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from tutorial_interfaces.srv import AddThreeInts


class CustomService(Node):

    def __init__(self):
        super().__init__('custom_addition_service')
        self.srv = self.create_service(
            AddThreeInts, 'add_three_ints', self.add_three_ints_callback)

    def add_three_ints_callback(self, request, response):
        response.sum = request.a + request.b + request.c
        self.get_logger().info(
            f'Incoming request: a={request.a} b={request.b} c={request.c}')
        return response


def main(args=None):
    try:
        with rclpy.init(args=args):
            rclpy.spin(CustomService())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
