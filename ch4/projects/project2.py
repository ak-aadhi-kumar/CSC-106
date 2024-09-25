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

# Expected output
#
# Enter a word: <sun>
# Enter a number: <5>
# - - - - sun
# - - - sun -
# - - sun - -
# - sun - - -
# sun - - - -

word = input('Enter a word: ')
number = input('Enter a number: ')

number = int(number)
output = ""
index = number-1
for i in range(number):
    output = ""
    for j in range(number):
        if j == index:
            output += word + " "
        else:
            output += "- "
    print(output)
    index -= 1

