import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Float64
from control_msgs.msg import JointControllerState
from ros2_control_interfaces.srv import ConfigureJointTrajectory

class ArmController(Node):
    def __init__(self):
        super().__init__('arm_controller')
        self.joint1_controller_pub = self.create_publisher(Float64, '/joint1_position_controller/command', 10)
        self.joint2_controller_pub = self.create_publisher(Float64, '/joint2_position_controller/command', 10)
        self.joint1_sub = self.create_subscription(JointControllerState, '/joint1_position_controller/state', self.joint1_callback, 10)
        self.joint2_sub = self.create_subscription(JointControllerState, '/joint2_position_controller/state', self.joint2_callback, 10)
        self.joint1_cmd = 0.0
        self.joint2_cmd = 0.0
        self.joint1_state = 0.0
        self.joint2_state = 0.0
        self.config_joint_trajectory()

    def joint1_callback(self, msg):
        self.joint1_state = msg.process_value

    def joint2_callback(self, msg):
        self.joint2_state = msg.process_value

    def config_joint_trajectory(self):
        self.configure_joint_trajectory_service = self.create_client(ConfigureJointTrajectory, '/configure_joint_trajectory')
        while not self.configure_joint_trajectory_service.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service /configure_joint_trajectory not available, waiting again...')
        request = ConfigureJointTrajectory.Request()
        request.joint_names = ['joint1', 'joint2']  # Modify according to your robot's joint names
        self.configure_joint_trajectory_service.call_async(request)

    def move_to_position(self, joint1_cmd, joint2_cmd):
        self.joint1_cmd = joint1_cmd
        self.joint2_cmd = joint2_cmd

    def servo_loop(self):
        joint1_msg = Float64()
        joint1_msg.data = self.joint1_cmd
        joint2_msg = Float64()
        joint2_msg.data = self.joint2_cmd
        self.joint1_controller_pub.publish(joint1_msg)
        self.joint2_controller_pub.publish(joint2_msg)

def main():
    rclpy.init()
    arm_controller = ArmController()

    # Example servoing loop
    while rclpy.ok():
        # Sample desired joint positions
        joint1_cmd = 1.5
        joint2_cmd = -0.5
        arm_controller.move_to_position(joint1_cmd, joint2_cmd)
        arm_controller.servo_loop()
        rclpy.spin_once(arm_controller)

    arm_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
