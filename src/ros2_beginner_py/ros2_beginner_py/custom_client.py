import sys

import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import AddThreeInts


class CustomClient(Node):

    def __init__(self):
        super().__init__('custom_addition_client')
        self.cli = self.create_client(AddThreeInts, 'add_three_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def send_request(self, a, b, c):
        request = AddThreeInts.Request()
        request.a = a
        request.b = b
        request.c = c
        return self.cli.call_async(request)


def main(args=None):
    with rclpy.init(args=args):
        client = CustomClient()
        a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
        future = client.send_request(a, b, c)
        rclpy.spin_until_future_complete(client, future)
        response = future.result()
        client.get_logger().info(f'Result: {a} + {b} + {c} = {response.sum}')


if __name__ == '__main__':
    main()
