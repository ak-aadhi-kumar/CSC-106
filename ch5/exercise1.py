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

sqft = float(input('Enter the square feet of wall to be painted: '))
ppg = float(input('Enter the price of paint per gallon: '))
gal = sqft/112
hrs = gal*8

print(f'Gallons of paint required: {gal}')
print(f'Hours of labour required: {hrs}')
print(f'Cost of paint: {gal*ppg}')
print(f'Labour charges: {hrs}')
print(f'Total cost: {hrs*35}')

