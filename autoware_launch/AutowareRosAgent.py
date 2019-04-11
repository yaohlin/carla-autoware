#!/usr/bin/env python
#
# Copyright (c) 2019 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#

from srunner.challenge.autoagents.ros_agent import RosAgent

class AutowareRosAgent(RosAgent):
    """
    Agent for Autoware ROS stack
    """

    def sensors(self):
        """
        The sensors required for Autoware
        """
        sensors = [
            {
                'type': 'sensor.camera.rgb',
                'id': 'front',
                'x': 2.0, 'y': 0.0, 'z': 2.0, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'width': 800, 'height': 600, 'fov':100
            },
            {
                'type': 'sensor.camera.rgb',
                'id': 'view',
                'x': 2.0, 'y': 0.0, 'z': 2.0, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                'width': 800, 'height': 600, 'fov': 100
            },
            {
                'type': 'sensor.lidar.ray_cast',
                'id': 'lidar1',
                'x': -0.15, 'y': 0.0, 'z': 2.6, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0
            },
            {
                'type': 'sensor.other.gnss',
                'id': 'gnss1',
                'x': 0.7, 'y': -0.4, 'z': 1.60
            },
            {
                'type': 'sensor.can_bus', 
                'id': 'can_bus',
                'reading_frequency': 25
            },
            {
                'type': 'sensor.hd_map',
                'id': 'hdmap',
                'reading_frequency': 25
            }
        ]

        return sensors

