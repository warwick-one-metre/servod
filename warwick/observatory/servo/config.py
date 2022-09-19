#
# This file is part of servod
#
# servod is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# servod is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with servod.  If not, see <http://www.gnu.org/licenses/>.

"""Helper function to validate and parse the json config file"""

import json
from warwick.observatory.common import daemons, IP, validation

CONFIG_SCHEMA = {
    'type': 'object',
    'additionalProperties': False,
    'required': ['daemon', 'log_name', 'control_machines', 'serial_port', 'serial_baud', 'serial_timeout',
                 'idle_loop_delay', 'moving_loop_delay', 'move_timeout', 'soft_step_limits'],
    'properties': {
        'daemon': {
            'type': 'string',
            'daemon_name': True
        },
        'log_name': {
            'type': 'string',
        },
        'control_machines': {
            'type': 'array',
            'items': {
                'type': 'string',
                'machine_name': True
            }
        },
        'serial_port': {
            'type': 'string',
        },
        'serial_baud': {
            'type': 'number',
            'min': 115200,
            'max': 115200
        },
        'serial_timeout': {
            'type': 'number',
            'min': 0
        },
        'idle_loop_delay': {
            'type': 'number',
            'min': 0
        },
        'moving_loop_delay': {
            'type': 'number',
            'min': 0
        },
        'move_timeout': {
            'type': 'number',
            'min': 0
        },
        'soft_step_limits': {
            'type': 'array',
            'maxItems': 2,
            'minItems': 2,
            'items': {
                'type': 'number'
            }
        }
    }
}


class Config:
    """Daemon configuration parsed from a json file"""
    def __init__(self, config_filename):
        # Will throw on file not found or invalid json
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            config_json = json.load(config_file)

        # Will throw on schema violations
        validation.validate_config(config_json, CONFIG_SCHEMA, {
            'daemon_name': validation.daemon_name_validator,
            'machine_name': validation.machine_name_validator,
        })

        self.daemon = getattr(daemons, config_json['daemon'])
        self.log_name = config_json['log_name']
        self.control_ips = [getattr(IP, machine) for machine in config_json['control_machines']]
        self.serial_port = config_json['serial_port']
        self.serial_baud = int(config_json['serial_baud'])
        self.serial_timeout = int(config_json['serial_timeout'])

        self.idle_loop_delay = int(config_json['idle_loop_delay'])
        self.moving_loop_delay = int(config_json['moving_loop_delay'])
        self.move_timeout = int(config_json['move_timeout'])
        self.soft_step_limits = [int(l) for l in config_json['soft_step_limits']]
