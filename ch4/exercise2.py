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

current = int(input('Starting number of organisms: '))
inc = input('Average daily increase: ')
days = int(input('Number of days to multiply: '))

inc = float(
    int(inc[0:2])/100
)

print('Day    Approximate Population')
print(f'1    {current}')
for i in range(2, days+1):
    current = current*(1+inc)
    print(f'{i}    {current}')

