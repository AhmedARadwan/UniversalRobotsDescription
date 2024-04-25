FROM ros:foxy-ros-base

RUN apt update

RUN /bin/bash -c "echo 'source /opt/ros/foxy/setup.bash' >> ~/.bashrc && source ~/.bashrc"
RUN rosdep update

# Install dependencies
RUN apt install -y ros-dev-tools \
                   build-essential \
                   cmake git \
                   libbullet-dev \
                   python3 \
                   python3-pip \
                   python3-colcon-common-extensions \
                   python3-flake8 \
                   python3-pip \
                   python3-pytest-cov \
                   python3-rosdep \
                   python3-setuptools \
                   python3-vcstool \
                   wget \
                   clang-format-10

# installing python dependancies
RUN pip3 install -U argcomplete \
                    flake8-blind-except \
                    flake8-builtins \
                    flake8-class-newline \
                    flake8-comprehensions \
                    flake8-deprecated \
                    flake8-docstrings \
                    flake8-import-order \
                    flake8-quotes \
                    pytest-repeat \
                    pytest-rerunfailures \
                    pytest \
                    cmake==3.22.0

# install requirements for moveit2 demos
RUN apt install -y ros-foxy-run-move-group
RUN apt install -y ros-foxy-run-ompl-constrained-planning
RUN apt install -y ros-foxy-moveit
RUN apt install -y ros-foxy-ros2-control ros-foxy-ros2-controllers
RUN apt install -y ros-foxy-ros-testing
RUN apt install -y freeglut3-dev \
                   libglew-dev \
                   ros-foxy-cv-bridge \
                   ros-foxy-image-transport \
                   ros-foxy-moveit-resources-fanuc-description \
                   ros-foxy-moveit-resources-fanuc-moveit-config \
                   ros-foxy-control-toolbox \
                   libfmt-dev librsl-dev \
                   ros-foxy-ur-msgs \
                   ros-foxy-ur-client-library
RUN apt install -y libyaml-cpp-dev ros-foxy-moveit-servo 
WORKDIR /home/workspace