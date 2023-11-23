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

import unittest
from unittest.mock import MagicMock

from GameStateMachine.engine import GameEngine
from GameStateMachine.states import BaseGameState


class MockGameState(BaseGameState):
    state_name = 'mock_state'

    def inputs(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def loop(self):
        pass

    def end(self):
        pass


class MockGameEngine(GameEngine):
    def init_states(self):
        MockGameState(target_state_name='mock_state2', state_manager=self, state_name='mock_state1')
        MockGameState(target_state_name=None, state_manager=self, state_name='mock_state2')


class TestGameEngine(unittest.TestCase):

    def setUp(self):
        self.engine = MockGameEngine(initial_state_name=None)

    def test_init(self):
        self.assertIsInstance(self.engine, GameEngine)
        self.assertEqual(len(self.engine.states), 2)
        self.assertIsNone(self.engine.active_state)

    def test_register_state(self):
        self.assertEqual(len(self.engine.states), 2)
        mock_state = MockGameState(target_state_name=None, state_manager=self.engine, state_name='mock_state3')
        self.assertEqual(len(self.engine.states), 3)
        self.assertEqual(self.engine.states[mock_state.name], mock_state)

    def test_set_initial_state(self):
        mock_state = MockGameState(target_state_name=None, state_manager=self.engine)
        self.engine.set_initial_state('mock_state')
        self.assertEqual(self.engine.active_state, mock_state)

    def test_set_initial_state_nonexistent(self):
        with self.assertRaises(NameError):
            self.engine.set_initial_state('nonexistent_state')

    def test_transition(self):
        mock_state3 = MockGameState(target_state_name='mock_state4', state_manager=self.engine, state_name='mock_state3')
        mock_state4 = MockGameState(target_state_name=None, state_manager=self.engine, state_name='mock_state4')

        mock_state3.end = MagicMock(return_value="transition_data")
        mock_state4.start = MagicMock()
        mock_state3.trigger_transition()
        self.engine.active_state = mock_state3
        self.assertIsNotNone(self.engine.active_state, 'Active state should not be None at this point')
        self.engine.transition()

        self.assertEqual(self.engine.active_state, mock_state4)
        mock_state3.end.assert_called_once()
        mock_state4.start.assert_called_once_with("transition_data")

    def test_exit(self):
        mock_state3 = MockGameState(target_state_name=None, state_manager=self.engine, state_name='mock_state3')
        self.engine.active_state = mock_state3

        mock_state3.end = MagicMock(return_value="exit_data")
        mock_state3.before_quit = MagicMock()

        with self.assertRaises(SystemExit):
            self.engine.exit()

        mock_state3.end.assert_called_once()
        mock_state3.before_quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
