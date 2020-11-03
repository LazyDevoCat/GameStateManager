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

from GameStateMachine.states import BaseGameState


class EmptyGameState(BaseGameState):

    state_name: str = 'loader'

    def __init__(self, target_state_name, state_manager):
        super().__init__(target_state_name, state_manager)
