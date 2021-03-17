# Copyright 2021
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Authors: Iñaki Lorente

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

#=====================================
#             VARIABLES
#=====================================
# Package (where to find configs)
pkg_name = 'ros2_camera'
# Folder inside package to find yaml
param_folder = 'config'
param_file = 'usb_conf.yaml'

#=====================================
#        LAUNCH CODE: USB-CAMERA
#=====================================
def generate_launch_description():

    # Parameters
    params_dir = os.path.join(get_package_share_directory(pkg_name),
                 	       param_folder,
                 	       param_file)

    return LaunchDescription([
        # Camera 
        Node(
            name='usb_streamer',
            package='ros2_camera',
            executable='usb_streamer',
            parameters=[params_dir],
            output='screen',
            emulate_tty=True)
    ])    

