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
with open('percentages.txt', 'r') as f:
    text = f.read()
text = text.split('\n')
sum1 = 0
for i in text:
    try: sum1 += float(i)
    except: continue
if 99.9 < sum1 < 100.1:
    percentage_check = True
else: percentage_check = False

