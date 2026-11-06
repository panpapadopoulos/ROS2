#!/usr/bin/env python3
from more_interfaces.msg import AddressBook
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class AddressBookPublisher(Node):

    def __init__(self):
        super().__init__('address_book_publisher')
        self.publisher = self.create_publisher(AddressBook, 'address_book', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = AddressBook()
        msg.first_name = 'John'
        msg.last_name = 'Doe'
        msg.phone_number = '1234567890'
        msg.phone_type = AddressBook.PHONE_TYPE_MOBILE
        self.get_logger().info(f'Publishing contact: {msg.first_name} {msg.last_name}')
        self.publisher.publish(msg)


def main(args=None):
    try:
        with rclpy.init(args=args):
            rclpy.spin(AddressBookPublisher())
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == '__main__':
    main()
