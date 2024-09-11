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

text = ''                                  
with open('units.txt', 'r') as f: 
    text = f.read()
text = text.split('-')

first_write = True
for i in text:
    a = i.split('\n')   
    sum1 = 0
    for j in a:
        try: sum1 += int(j)
        except: pass
    if first_write:
        with open('totals.txt', 'w') as f:
            f.write(f'{sum1}')  
        first_write = False
    else:
        with open('totals.txt', 'a') as f:
            f.write(f'\n{sum1}')

