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

"""Game State Machine is a wrapper class set of Python classes and modules
that help manage game and game states. For instance, during game running
you would need several states (splash screen, loading screen,
menu screen, lobby screen etc.), so you can easily manage all of them
by creating classes from BaseGameState"""

from GameStateMachine.engine import GameEngine

__all__ = ['GameEngine']
