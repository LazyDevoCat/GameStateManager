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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("version.txt", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="GameStateMachine",
    version=version,
    author="Oleksii Bulba",
    author_email="oleksii.bulba+gamestatemachine@gmail.com",
    description="Game state machine - provides a game management based on a game state",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OleksiiBulba/GameStateManager",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
    ],
    python_requires='>=3.7.17'
)
