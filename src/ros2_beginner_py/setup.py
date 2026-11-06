from glob import glob

from setuptools import find_packages, setup

package_name = 'ros2_beginner_py'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Panagiotis Papadopoulos',
    maintainer_email='papadop@purdue.edu',
    description='ROS 2 beginner tutorials in Python',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'publisher = ros2_beginner_py.publisher:main',
            'subscriber = ros2_beginner_py.subscriber:main',
            'service = ros2_beginner_py.service:main',
            'client = ros2_beginner_py.client:main',
            'parameters = ros2_beginner_py.parameters:main',
            'custom_publisher = ros2_beginner_py.custom_publisher:main',
            'custom_subscriber = ros2_beginner_py.custom_subscriber:main',
            'custom_service = ros2_beginner_py.custom_service:main',
            'custom_client = ros2_beginner_py.custom_client:main',
        ],
    },
)
