import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class Client(Node):

    def __init__(self):
        super().__init__('addition_client')
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

    def send_request(self, a, b):
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        return self.cli.call_async(request)


def main(args=None):
    with rclpy.init(args=args):
        client = Client()
        a, b = int(sys.argv[1]), int(sys.argv[2])
        future = client.send_request(a, b)
        rclpy.spin_until_future_complete(client, future)
        response = future.result()
        client.get_logger().info(f'Result: {a} + {b} = {response.sum}')


if __name__ == '__main__':
    main()
