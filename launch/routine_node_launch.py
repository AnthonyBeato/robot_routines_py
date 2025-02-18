from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_routines_py',
            executable='routine_node',
            name='routine_node',
            output='screen',
        ),
    ])
