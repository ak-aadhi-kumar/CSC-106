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

nums = input('Enter 20 numbers seperated by commas (no spaces): ')
nums = nums.split(',')


index = 0
for n in nums:
    nums[index] = float(n)
    index += 1

nums.sort()

total = 0
for n in nums:
    total += n

print(f'The lowest number is: {nums[0]}')
print(f'The highest number is: {nums[19]}')
print(f'The total of the numbers is: {total}')
print(f'The average of the numbers is: {total/20}')

