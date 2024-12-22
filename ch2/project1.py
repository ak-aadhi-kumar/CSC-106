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

num_loaves = float(input('How many loaves do you want to make? '))

warm_water = round(float(1.5*num_loaves), 1)
yeast = round(float(num_loaves), 1)
ap_flour = round(float(4.5*num_loaves), 1)
oil = round(float(2*num_loaves), 1)

print(f'You need {warm_water} cups of warm water, {yeast} tablespoons of yeast, {ap_flour} cups of all-purpose flour, and {oil} tablespoons of oil.')

