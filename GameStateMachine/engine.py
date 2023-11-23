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

from abc import abstractmethod, ABC
import sys

import logging
from typing import Union

from GameStateMachine.states import BaseGameState


class GameEngine(ABC):
    """
    Basic Game Engine class. It manages all the game states.
    To create a Game class that inherits GameEngine, your Game class needs to implement the method init_states that
    initializes all game states that inherits BaseGameState, BaseGameState class contains a call to register_state here,
    so all created game states will auto registered here.
    """

    def __init__(self, initial_state_name: Union[str, None]):
        self.states = {}
        self.active_state: Union[BaseGameState, None] = None
        self.init_states()
        if initial_state_name is not None:
            self.set_initial_state(initial_state_name)

    @abstractmethod
    def init_states(self) -> None:
        """
        Initializes states, return nothing
        :return: None
        """
        raise NotImplementedError(f'{__name__} method should be implemented in child classes')

    def set_initial_state(self, state_name):
        if state_name in self.states.keys():
            self.active_state = self.states[state_name]
        else:
            raise NameError(f'State name {state_name} not found. Did you forget to initialize it?')

    def register_state(self, state: BaseGameState):
        if state.name not in self.states:
            self.states[state.name] = state
        else:
            raise NameError(f'State {state.name} already exists')

    def run(self):
        while True:
            if self.active_state is None:
                raise ValueError('Active state is not defined')

            if not self.active_state.started:
                self.active_state.start()

            self.active_state.run()

            if self.active_state.time_to_quit_app:
                break

            if self.active_state.time_to_transition:
                self.transition()

        self.exit()

    def transition(self):
        new_state_name = self.active_state.target_state_name
        logging.info(f'Transition from "{self.active_state.name}" -> to "{new_state_name}"')
        self.active_state.time_to_transition = False
        transitioning_data = self.active_state.end()
        self.active_state = self.states[new_state_name]
        self.active_state.start(transitioning_data)

    def exit(self):
        self.active_state.end()
        for state in self.states.values():
            state.before_quit()
        sys.exit()
