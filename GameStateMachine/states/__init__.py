#  GameStateManager - provides a game management based on a game state
#  Copyright (C) 2020-2023  Oleksii Bulba
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
#
#  Oleksii Bulba
#  oleksii.bulba+gamestatemachine@gmail.com

from abc import ABC, abstractmethod
from typing import Any, Union


class BaseGameState(ABC):
    state_name: str = 'base'

    def __init__(self, target_state_name: Union[str, None], state_manager, state_name: str = None):
        self.name = state_name if state_name is not None else self.state_name
        self.target_state_name = target_state_name
        self.state_manager = state_manager
        self.started = False
        self.time_to_transition = False
        self.time_to_quit_app = False
        self.state_manager.register_state(self)

    def set_target_state_name(self, target_name):
        """
        Target name is a target state name that will be used to transition to in case current game state will trigger.
        transitioning
        """
        self.target_state_name = target_name

    def trigger_transition(self, target_state_name: str = None):
        self.time_to_transition = True
        target_state_name = target_state_name if target_state_name is not None else self.target_state_name
        assert target_state_name is not None, 'target state name cannot be None'
        self.target_state_name = target_state_name

    def start(self, incoming_data: Any = None):
        """
        Process here any incoming data,
        don't forget to call "super().start()" method or set "self.started" to True otherwise.
        """
        self.started = True

    def run(self):
        while True:
            self.inputs()
            self.update()
            self.draw()
            self.loop()

    @abstractmethod
    def inputs(self):
        """Processing all inputs from the user (mouse, keyboard, timer, etc. events)"""
        pass

    @abstractmethod
    def update(self):
        """Update everything here"""
        pass

    @abstractmethod
    def draw(self):
        """Draw everything here"""
        pass

    @abstractmethod
    def loop(self):
        """Define how fast your loop should run here"""
        pass

    @abstractmethod
    def end(self) -> Any:
        """Process any outgoing data here"""
        pass

    def before_quit(self):
        """The method will be run before the whole app is quiting"""
        pass

    def quit(self):
        """Trigger quiting from the app"""
        self.time_to_quit_app = True
