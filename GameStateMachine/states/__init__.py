# game state machine - provides a game management based on a game state
# Copyright (C) 2020  Oleksii Bulba
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Oleksii Bulba
# oleksii.bulba@gmail.com


class BaseGameState(object):

    state_name: str = 'base'

    def __init__(self, target_state_name, state_manager):
        self.name = self.state_name
        self.target_state_name = target_state_name
        self.outgoing_transition_data = {}
        self.incoming_transition_data = {}
        self.state_manager = state_manager
        self.time_to_transition = False
        self.time_to_quit_app = False
        self.state_manager.register_state(self)

    def set_target_state_name(self, target_name):
        self.target_state_name = target_name

    def trigger_transition(self, target_state_name: str = None):
        self.time_to_transition = True
        if target_state_name is not None:
            self.target_state_name = target_state_name

    def run(self, time_delta):
        pass

    def end(self):
        pass

    def quit(self):
        self.time_to_quit_app = True
