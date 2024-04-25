cmake_minimum_required(VERSION 3.5)
project(arm_control)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(control_msgs REQUIRED)

# Install Python executables
install(PROGRAMS
  scripts/arm_control_test.py
  DESTINATION lib/${PROJECT_NAME}
)
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

# Export dependencies
ament_export_dependencies(rclpy std_msgs control_msgs)

ament_package()
