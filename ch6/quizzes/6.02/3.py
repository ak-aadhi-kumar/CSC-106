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
with open('grade.txt', 'r') as f: 
    text = f.read()
text = text.split('\n')

def append_file(filename, text):   
    with open(filename, 'a') as f:
        f.write(f'{text}\n')

passed = 0
total = 0
for i in text:      
    i = int(i)
    if i >= 6:      
        append_file('passing.txt', i)    
        passed += 1 
    elif i < 6:
        append_file('failing.txt', i)    
    total += 1

with open('statistics.txt', 'w') as f:
    f.write(str(round(passed/total*100, 2)))

