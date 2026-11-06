from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='ros2_beginner_py', executable='publisher',
             output='screen'),
        Node(package='ros2_beginner_py', executable='subscriber',
             output='screen'),
    ])
