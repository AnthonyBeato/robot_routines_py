import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class RoutineNode(Node):

    def __init__(self):
        super().__init__('routine_node')
        self.cmd_vel_pub = self.create_publisher(Twist, '/robot_1/diffbot_base_controller/cmd_vel_unstamped', 10)
        self.timer = self.create_timer(0.1, self.execute_routine)

        # Inicio de configuracion de variables 
        # TODO: Poner tus variables
        self.start_time = self.get_clock().now()
        self.distance_traveled = 0.0
        self.target_duration = 10.0  # Limitar a 3 segundos
        # Fin de configuracion de variables

        self.get_logger().info('Routine node has been started.')

    def execute_routine(self):
        msg = Twist()
        # TODO: Implementa la logica de la rutina aqui
        # Ejemplo: Mover hacia delante durante 1 metro
        elapsed_time = (self.get_clock().now() - self.start_time).nanoseconds / 1e9
        if elapsed_time < self.target_duration:
            # Mover hacia delante en linea recta
            msg.linear.x = 0.1
            msg.angular.z = 0.0
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.cmd_vel_pub.publish(msg)

        # Agregar logica adicional a la rutina como se necesite


def main(args=None):
    rclpy.init(args=args)
    node = RoutineNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
