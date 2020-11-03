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
import time


class Clock(object):
    def __init__(self):
        self.now_time = self.last_tick = time.time()
        self.time_passed = None
        self.fps_count = 0
        self.fps_tick = None

    def tick(self, frame_rate: int):
        if frame_rate > 0:
            time.sleep(frame_rate / 1000.0)
        now_time = time.time()
        self.time_passed = now_time - self.last_tick
        self.fps_count += 1
        self.last_tick = now_time

        if self.fps_tick is None:
            self.fps_count = 0
            self.fps_tick = now_time

        return self.time_passed
