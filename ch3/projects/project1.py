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

number = float(input())

if number%1 != 0 or number <= 0:
    print('You can only input positive integers.')
elif number%2 == 0 and number%3 == 0 and number%5 == 0:
    print('The number is magic!')
else: print('The number is not magic.')
