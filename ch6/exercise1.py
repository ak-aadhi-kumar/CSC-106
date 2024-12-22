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

file_read = ''
try:
    with open('numbers.txt', 'r') as f:
        file_read = f.read()
except: print('Unable to read file')
else:
    file_read = file_read.split('\n')
    file_read.pop()
    sum1 = 0
    count = 0
    for num in file_read:
        sum1 += float(num)
        count += 1
    avg = sum1/count

    print(f'The average of all the numbers is: {avg}')

