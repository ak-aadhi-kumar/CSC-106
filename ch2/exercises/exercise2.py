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

amount = float(input('Enter the amount of a purchase: '))

state = amount*0.05
county = amount*0.025

print(f'Amount of purchase: {amount}')
print(f'State sales tax: {state}')
print(f'County sales tax: {county}')
print(f'Total sales tax: {state+county}')
print(f'Grand total: {amount+state+county}')

