# Copyright (C) 2024 Aadhi Kumar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# predefined
# daily_penguin_ration = 2
# daily_seal_ration = 4
# daily_polar_bear_ration = 5

penguins = int(input('Enter the number of penguins: '))
seals = int(input('Enter the number of seals: '))
p_bears = int(input('Enter the number of polar bears: '))

penguins_food = int(round(30*daily_penguin_ration*penguins, 0))
seals_food = int(round(30*daily_seal_ration*seals, 0))
p_bears_food = int(round(30*daily_polar_bear_ration*p_bears, 0))

print(f'The food consumed by penguins is {penguins_food} kg')
print(f'The food consumed by seals is {seals_food} kg')
print(f'The food consumed by polar bears is {p_bears_food} kg')

