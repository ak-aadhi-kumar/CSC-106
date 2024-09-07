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

colour1 = input('Enter first colour to mix: ')
colour2 = input('Enter second colour to mix: ')

if not (
    (colour1 == 'red' or colour1 == 'yellow' or colour1 == 'blue') and \
    (colour2 == 'red' or colour2 == 'yellow' or colour2 == 'blue')
): print('Error: Only mixing red, yellow, and blue is supported.')

else:
    if (colour1 == 'red' and colour2 == 'yellow') or \
        (colour1 == 'yellow' and colour2 == 'red'):
            print('You will get orange')
    elif (colour1 == 'red' and colour2 == 'blue') or \
        (colour1 == 'blue' and colour2 == 'red'):
            print('You will get purple')
    elif (colour1 == 'yellow' and colour2 == 'blue') or \
        (colour1 == 'blue' and colour2 == 'yellow'):
            print('You will get green')

