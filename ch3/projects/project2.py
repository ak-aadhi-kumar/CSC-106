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

first_colour = input('Enter the first color: ')
second_colour = input('Enter the second color: ')

approved_colours = ['red', 'green', 'yellow', 'purple', 'blue', 'orange']

a = False
b = False
for colour in approved_colours:
    if colour == first_colour:
        a = True
    elif colour == second_colour:
        b = True

if not (a and b):
    print('You did not enter one of red, orange, yellow, green, blue or purple')

elif (first_colour == 'red' and second_colour == 'green') or \
    (first_colour == 'green' and second_colour == 'red'):
        print('The two colors are complementary')

elif (first_colour == 'yellow' and second_colour == 'purple') or \
    (first_colour == 'purple' and second_colour == 'yellow'):
        print('The two colors are complementary')

elif (first_colour == 'blue' and second_colour == 'orange') or \
    (first_colour == 'orange' and second_colour == 'blue'):
        print('The two colors are complementary')

else: print('The two colors are not complementary')

