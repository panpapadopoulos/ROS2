from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('greeting', default_value='world'),
        Node(
            package='ros2_beginner_py', executable='parameters',
            parameters=[{'my_parameter': LaunchConfiguration('greeting')}],
            output='screen'),
    ])
